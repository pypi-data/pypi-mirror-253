from __future__ import annotations

import argparse
from collections import Counter

from loguru import logger

from errant.metrics.criteria import computeFScore
from errant.utils.helper import merge_dict
from errant.utils.pretty_results import print_results, print_table


def main():
    # Parse command line args
    args = parse_args()
    # Open hypothesis and reference m2 files and split into chunks
    hyp_m2 = open(args.hyp).read().strip().split("\n\n")
    ref_m2 = open(args.ref).read().strip().split("\n\n")
    # Make sure they have the same number of sentences
    assert len(hyp_m2) == len(ref_m2)

    # Store global corpus level best counts here
    best_dict = Counter({"tp": 0, "fp": 0, "fn": 0})
    best_cats = {}
    # Process each sentence
    sents = zip(hyp_m2, ref_m2)
    for sent_id, sent in enumerate(sents):
        # Simplify the edits into lists of lists
        hyp_edits = simplify_edits(sent[0])
        ref_edits = simplify_edits(sent[1])
        # Process the edits for detection/correction based on args
        hyp_dict = process_edits(hyp_edits, args)
        ref_dict = process_edits(ref_edits, args)
        # original sentence for logging
        original_sentence = sent[0][2:].split("\nA")[0]
        # Evaluate edits and get best TP, FP, FN hyp+ref combo.
        count_dict, cat_dict = evaluate_edits(
            hyp_dict,
            ref_dict,
            best_dict,
            sent_id,
            original_sentence,
            args,
        )
        # Merge these dicts with best_dict and best_cats
        best_dict += Counter(count_dict)
        best_cats = merge_dict(best_cats, cat_dict)
    logger.info("Systematic Evaluate based on ERRANT tags")
    print_results(best_dict, best_cats, args.dt, args.ds, args.cse, args.cat, args.beta)


# Parse command line args


def parse_args():
    parser = argparse.ArgumentParser(
        description="Calculate F-scores for error detection and/or correction.\n"
        "Flags let you evaluate at different levels of granularity.",
        formatter_class=argparse.RawTextHelpFormatter,
        usage="%(prog)s [options] -hyp HYP -ref REF",
    )
    parser.add_argument("-hyp", help="A hypothesis M2 file.", required=True)
    parser.add_argument("-ref", help="A reference M2 file.", required=True)
    parser.add_argument(
        "-b",
        "--beta",
        help="Value of beta in F-score. (default: 0.5)",
        default=0.5,
        type=float,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="Print verbose output.",
        action="store_true",
    )
    eval_type = parser.add_mutually_exclusive_group()
    eval_type.add_argument(
        "-dt",
        help="Evaluate Detection in terms of Tokens.",
        action="store_true",
    )
    eval_type.add_argument(
        "-ds",
        help="Evaluate Detection in terms of Spans.",
        action="store_true",
    )
    eval_type.add_argument(
        "-cs",
        help="Evaluate Correction in terms of Spans. (default)",
        action="store_true",
    )
    eval_type.add_argument(
        "-cse",
        help="Evaluate Correction in terms of Spans and Error types.",
        action="store_true",
    )
    parser.add_argument(
        "-single",
        help="Only evaluate single token edits; i.e. 0:1, 1:0 or 1:1",
        action="store_true",
    )
    parser.add_argument(
        "-multi",
        help="Only evaluate multi token edits; i.e. 2+:n or n:2+",
        action="store_true",
    )
    parser.add_argument(
        "-filt",
        help="Do not evaluate the specified error types.",
        nargs="+",
        default=[],
    )
    parser.add_argument(
        "-cat",
        help="Show error category scores.\n"
        "1: Only show operation tier scores; e.g. R.\n"
        "2: Only show main tier scores; e.g. NOUN.\n"
        "3: Show all category scores; e.g. R:NOUN.",
        choices=[1, 2, 3],
        type=int,
    )
    args = parser.parse_args()
    return args


# Input: An m2 format sentence with edits.
# Output: A list of lists. Each edit: [start, end, cat, cor, coder]
def simplify_edits(sent):
    out_edits = []
    # Get the edit lines from an m2 block.
    edits = sent.split("\n")[1:]
    # Loop through the edits
    for edit in edits:
        # Preprocessing
        edit = edit[2:].split("|||")  # Ignore "A " then split.
        span = edit[0].split()
        start = int(span[0])
        end = int(span[1])
        cat = edit[1]
        cor = edit[2]
        coder = int(edit[-1])
        out_edit = [start, end, cat, cor, coder]
        out_edits.append(out_edit)
    return out_edits


# Input 1: A list of edits. Each edit: [start, end, cat, cor, coder]
# Input 2: Command line args
# Output: A dict; key is coder, value is edit dict.
def process_edits(edits, args):
    coder_dict = {}
    # Add an explicit noop edit if there are no edits.
    if not edits:
        edits = [[-1, -1, "noop", "-NONE-", 0]]
    # Loop through the edits
    for edit in edits:
        # Name the edit elements for clarity
        start = edit[0]
        end = edit[1]
        cat = edit[2]
        cor = edit[3]
        coder = edit[4]
        # Add the coder to the coder_dict if necessary
        if coder not in coder_dict:
            coder_dict[coder] = {}

        # Optionally apply filters based on args
        # 1. UNK type edits are only useful for detection, not correction.
        if not args.dt and not args.ds and cat == "UNK":
            continue
        # 2. Only evaluate single token edits; i.e. 0:1, 1:0 or 1:1
        if args.single and (end - start >= 2 or len(cor.split()) >= 2):
            continue
        # 3. Only evaluate multi token edits; i.e. 2+:n or n:2+
        if args.multi and end - start < 2 and len(cor.split()) < 2:
            continue
        # 4. If there is a filter, ignore the specified error types
        if args.filt and cat in args.filt:
            continue

        # Token Based Detection
        if args.dt:
            # Preserve noop edits.
            if start == -1:
                if (start, start) in coder_dict[coder].keys():
                    coder_dict[coder][(start, start)].append(cat)
                else:
                    coder_dict[coder][(start, start)] = [cat]
            # Insertions defined as affecting the token on the right
            elif start == end and start >= 0:
                if (start, start + 1) in coder_dict[coder].keys():
                    coder_dict[coder][(start, start + 1)].append(cat)
                else:
                    coder_dict[coder][(start, start + 1)] = [cat]
            # Edit spans are split for each token in the range.
            else:
                for tok_id in range(start, end):
                    if (tok_id, tok_id + 1) in coder_dict[coder].keys():
                        coder_dict[coder][(tok_id, tok_id + 1)].append(cat)
                    else:
                        coder_dict[coder][(tok_id, tok_id + 1)] = [cat]

        # Span Based Detection
        elif args.ds:
            if (start, end) in coder_dict[coder].keys():
                coder_dict[coder][(start, end)].append(cat)
            else:
                coder_dict[coder][(start, end)] = [cat]

        # Span Based Correction
        else:
            # With error type classification
            if args.cse:
                if (start, end, cat, cor) in coder_dict[coder].keys():
                    coder_dict[coder][(start, end, cat, cor)].append(cat)
                else:
                    coder_dict[coder][(start, end, cat, cor)] = [cat]
            # Without error type classification
            else:
                if (start, end, cor) in coder_dict[coder].keys():
                    coder_dict[coder][(start, end, cor)].append(cat)
                else:
                    coder_dict[coder][(start, end, cor)] = [cat]
    return coder_dict


# Input 1: A hyp dict; key is coder_id, value is dict of processed hyp edits.
# Input 2: A ref dict; key is coder_id, value is dict of processed ref edits.
# Input 3: A dictionary of the best corpus level TP, FP and FN counts so far.
# Input 4: Sentence ID (for verbose output only)
# Input 5: Command line args
# Output 1: A dict of the best corpus level TP, FP and FN for the input sentence.
# Output 2: The corresponding error type dict for the above dict.
def evaluate_edits(hyp_dict, ref_dict, best, sent_id, original_sentence, args):
    # Verbose output: display the original sentence
    if args.verbose:
        print("{:-^40}".format(""))
        print("Original sentence " + str(sent_id) + ": " + original_sentence)
    # Store the best sentence level scores and hyp+ref combination IDs
    # best_f is initialised as -1 cause 0 is a valid result.
    best_tp, best_fp, best_fn, best_f, best_hyp, best_ref = 0, 0, 0, -1, 0, 0
    best_cat = {}
    # Compare each hyp and ref combination
    for hyp_id in hyp_dict.keys():
        for ref_id in ref_dict.keys():
            # Get the local counts for the current combination.
            tp, fp, fn, cat_dict = compareEdits(
                hyp_dict[hyp_id],
                ref_dict[ref_id],
            )
            # Compute the local sentence scores (for verbose output only)
            loc_p, loc_r, loc_f = computeFScore(tp, fp, fn, args.beta)
            # Compute the global sentence scores
            p, r, f = computeFScore(
                tp + best["tp"],
                fp + best["fp"],
                fn + best["fn"],
                args.beta,
            )
            # Save the scores if they are better in terms of:
            # 1. Higher F-score
            # 2. Same F-score, higher TP
            # 3. Same F-score and TP, lower FP
            # 4. Same F-score, TP and FP, lower FN
            if (
                (f > best_f)
                or (f == best_f and tp > best_tp)
                or (f == best_f and tp == best_tp and fp < best_fp)
                or (f == best_f and tp == best_tp and fp == best_fp and fn < best_fn)
            ):
                best_tp, best_fp, best_fn = tp, fp, fn
                best_f, best_hyp, best_ref = f, hyp_id, ref_id
                best_cat = cat_dict
            # Verbose output
            if args.verbose:
                # Prepare verbose output edits.
                hyp_verb = list(sorted(hyp_dict[hyp_id].keys()))
                ref_verb = list(sorted(ref_dict[ref_id].keys()))
                # add categories
                # hyp_dict[hyp_id] looks like (0, 1, "str")
                # hyp_dict[hyp_id][h] is a list, always length one, of the corresponding category
                hyp_verb = [h + (hyp_dict[hyp_id][h][0],) for h in hyp_verb]
                ref_verb = [r + (ref_dict[ref_id][r][0],) for r in ref_verb]
                # Ignore noop edits
                if not hyp_verb or hyp_verb[0][0] == -1:
                    hyp_verb = []
                if not ref_verb or ref_verb[0][0] == -1:
                    ref_verb = []
                # Print verbose info
                print("{:-^40}".format(""))
                print(
                    "SENTENCE "
                    + str(sent_id)
                    + " - HYP "
                    + str(hyp_id)
                    + " - REF "
                    + str(ref_id),
                )
                print("HYPOTHESIS EDITS :", hyp_verb)
                print("REFERENCE EDITS  :", ref_verb)
                print("Local TP/FP/FN   :", str(tp), str(fp), str(fn))
                print(
                    "Local P/R/F" + str(args.beta) + "  :",
                    str(loc_p),
                    str(loc_r),
                    str(loc_f),
                )
                print(
                    "Global TP/FP/FN  :",
                    str(tp + best["tp"]),
                    str(fp + best["fp"]),
                    str(fn + best["fn"]),
                )
                print(
                    "Global P/R/F" + str(args.beta) + "  :",
                    str(p),
                    str(r),
                    str(f),
                )
    # Verbose output: display the best hyp+ref combination
    if args.verbose:
        print("{:-^40}".format(""))
        print(
            "^^ HYP "
            + str(best_hyp)
            + ", REF "
            + str(best_ref)
            + " chosen for sentence "
            + str(sent_id),
        )
        print("Local results:")
        header = ["Category", "TP", "FP", "FN"]
        body = [[k, *v] for k, v in best_cat.items()]
        print_table([header] + body)
    # Save the best TP, FP and FNs as a dict, and return this and the best_cat dict
    best_dict = {"tp": best_tp, "fp": best_fp, "fn": best_fn}
    return best_dict, best_cat


# Input 1: A dictionary of hypothesis edits for a single system.
# Input 2: A dictionary of reference edits for a single annotator.
# Output 1-3: The TP, FP and FN for the hyp vs the given ref annotator.
# Output 4: A dictionary of the error type counts.
def compareEdits(hyp_edits, ref_edits):
    tp = 0  # True Positives
    fp = 0  # False Positives
    fn = 0  # False Negatives
    cat_dict = {}  # {cat: [tp, fp, fn], ...}

    for h_edit, h_cats in hyp_edits.items():
        # noop hyp edits cannot be TP or FP
        if h_cats[0] == "noop":
            continue
        # TRUE POSITIVES
        if h_edit in ref_edits.keys():
            # On occasion, multiple tokens at same span.
            for h_cat in ref_edits[h_edit]:  # Use ref dict for TP
                tp += 1
                # Each dict value [TP, FP, FN]
                if h_cat in cat_dict.keys():
                    cat_dict[h_cat][0] += 1
                else:
                    cat_dict[h_cat] = [1, 0, 0]
        # FALSE POSITIVES
        else:
            # On occasion, multiple tokens at same span.
            for h_cat in h_cats:
                fp += 1
                # Each dict value [TP, FP, FN]
                if h_cat in cat_dict.keys():
                    cat_dict[h_cat][1] += 1
                else:
                    cat_dict[h_cat] = [0, 1, 0]
    for r_edit, r_cats in ref_edits.items():
        # noop ref edits cannot be FN
        if r_cats[0] == "noop":
            continue
        # FALSE NEGATIVES
        if r_edit not in hyp_edits.keys():
            # On occasion, multiple tokens at same span.
            for r_cat in r_cats:
                fn += 1
                # Each dict value [TP, FP, FN]
                if r_cat in cat_dict.keys():
                    cat_dict[r_cat][2] += 1
                else:
                    cat_dict[r_cat] = [0, 0, 1]
    return tp, fp, fn, cat_dict


if __name__ == "__main__":
    # Run the program
    main()
