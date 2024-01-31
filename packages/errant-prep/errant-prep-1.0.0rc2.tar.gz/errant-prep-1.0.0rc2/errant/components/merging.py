from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from errant.components.alignment import Alignment


class BaseMerger(ABC):
    """
    Base class for all merging classes.
    """

    def __init__(self):
        pass

    
    @abstractmethod
    def process(self, alignment: Alignment):
        """
        Process an alignment into a list of edits.
        :param alignment: An Alignment object.
        :return: A list of Edit objects.
        """
        raise NotImplementedError

    @staticmethod
    def merge_edits(edit):
        """
        Merge a list of edits into a single edit.
        :param edit: A list of edits to merge.
        :return: A single merged edit.
        """
        raise NotImplementedError
