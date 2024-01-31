from __future__ import annotations


def noop_edit(id: int = 0) -> str:
    """
    Create a noop edit string.
    :param id: The id number of the annotation.
    :return: A noop edit string.
    """
    return "A -1 -1|||noop|||-NONE-|||REQUIRED|||-NONE-|||" + str(id)


class Edit:
    """
    An object representing an edit.
    """

    def __init__(self, orig: str, cor: str, edit: list, type="NA"):
        """
        Initialise the edit object with the orig and cor token spans and
        the error type. If the error type is not known, it is set to "NA".
        :param orig: The original text string parsed by spacy.
        :param cor: The corrected text string parsed by spacy.
        :param edit: A token span edit list: [o_start, o_end, c_start, c_end].
        :param type: The error type string, if known.
        """
        # Orig offsets, spacy tokens and string
        self.o_start = edit[0]
        self.o_end = edit[1]
        self.o_toks = orig[self.o_start : self.o_end]
        self.o_str = self.o_toks.text if self.o_toks else ""
        # Cor offsets, spacy tokens and string
        self.c_start = edit[2]
        self.c_end = edit[3]
        self.c_toks = cor[self.c_start : self.c_end]
        self.c_str = self.c_toks.text if self.c_toks else ""
        # Error type
        self.type = type

    # Minimise the edit; e.g. [a b -> a c] = [b -> c]
    def minimise(self):
        """
        Minimise the edit by removing common tokens from the start and end of
        the edit spans. This is done by adjusting the start and end offsets
        and removing tokens from the token spans.
        :return: The minimised edit object.
        Examples:
            >>> e = Edit("a b c", "a d c", [0, 3, 0, 3])
            >>> print(e)
            Orig: [0, 3, 'a b c'], Cor: [0, 3, 'a d c'], Type: 'NA'
            >>> e.minimise()
            >>> print(e)
            Orig: [1, 2, 'b'], Cor: [1, 2, 'd'], Type: 'NA'
        """
        # While the first token is the same on both sides
        while (
            self.o_toks and self.c_toks and self.o_toks[0].text == self.c_toks[0].text
        ):
            # Remove that token from the span, and adjust the start offsets
            self.o_toks = self.o_toks[1:]
            self.c_toks = self.c_toks[1:]
            self.o_start += 1
            self.c_start += 1
        # Do the same for the last token
        while (
            self.o_toks and self.c_toks and self.o_toks[-1].text == self.c_toks[-1].text
        ):
            self.o_toks = self.o_toks[:-1]
            self.c_toks = self.c_toks[:-1]
            self.o_end -= 1
            self.c_end -= 1
        # Update the strings
        self.o_str = self.o_toks.text if self.o_toks else ""
        self.c_str = self.c_toks.text if self.c_toks else ""
        return self

    def to_m2(self, id=0):
        """
        Convert the edit to an m2 string. If the error type is "NA", it is
        converted to "UNK".
        :param id: The id number of the annotation.
        """
        span = " ".join(["A", str(self.o_start), str(self.o_end)])
        cor_toks_str = " ".join([tok.text for tok in self.c_toks])
        return "|||".join(
            [span, self.type, cor_toks_str, "REQUIRED", "-NONE-", str(id)],
        )

    # Edit object string representation
    def __str__(self):
        """
        Print the edit object in a readable format.
        """
        orig = "Orig: " + str([self.o_start, self.o_end, self.o_str])
        cor = "Cor: " + str([self.c_start, self.c_end, self.c_str])
        type = "Type: " + repr(self.type)
        return ", ".join([orig, cor, type])
