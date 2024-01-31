from __future__ import annotations

from pathlib import Path

import spacy.symbols as POS

from errant.components.en.lancaster import LancasterStemmer
from errant.components.en.utils import load_pos_map, load_word_list

# Classifier resources
base_dir = Path(__file__).resolve().parent
# Spacy
nlp = None
# Lancaster Stemmer
stemmer = LancasterStemmer()
# GB English word list (inc -ise and -ize)
spell = load_word_list(base_dir / "resources" / "en_GB-large.txt")
# Part of speech map file
pos_map = load_pos_map(base_dir / "resources" / "en-ptb_map")
# Open class coarse Spacy POS tags
open_pos1 = {POS.ADJ, POS.ADV, POS.NOUN, POS.VERB}
# Open class coarse Spacy POS tags (strings)
open_pos2 = {"ADJ", "ADV", "NOUN", "VERB"}
# Rare POS tags that make uninformative error categories
rare_pos = {"INTJ", "NUM", "SYM", "X"}
# Contractions
conts = {"'d", "'ll", "'m", "n't", "'re", "'s", "'ve"}
# Special auxiliaries in contractions.
aux_conts = {"ca": "can", "sha": "shall", "wo": "will"}
# Some dep labels that map to pos tags.
dep_map = {
    "acomp": "ADJ",
    "amod": "ADJ",
    "advmod": "ADV",
    "det": "DET",
    "prep": "PREP",
    "prt": "PART",
    "punct": "PUNCT",
}
