from __future__ import annotations

from abc import ABC
from abc import abstractmethod

class BaseClassifer(ABC):
    """
    Abstract class for a classifier.
    """
    def __init__(self):
        pass

    @abstractmethod
    def classify(self, edit):
        """
        Classify an edit.

        Args:
            edit: An Edit object.

        Returns:
            A string label for the edit.
        """
        raise NotImplementedError
