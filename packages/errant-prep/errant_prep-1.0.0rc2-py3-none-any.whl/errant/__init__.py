from __future__ import annotations

from importlib import import_module
from typing import Any

import spacy

from errant.annotator import Annotator
from errant.utils.utils import get_spacy_models_for_language

# ERRANT version
__version__ = 'v1.0.0rc2'


# Load an ERRANT Annotator object for a given language
def load(
    lang: str = 'en', model_name: str = 'en_core_web_sm', nlp: Any = None,
) -> Annotator:
    """
    Load an ERRANT Annotator object for a given language.
    :param lang: The language code (e.g., 'en' for English) to load.
    :param model_name: The spaCy model name to load.
    :param nlp: The spaCy model object to load.
    :return: An Annotator object.
    """
    # Make sure the language is supported
    supported = {'en'}  # TODO for other languages. English only for now.
    if lang not in supported:
        raise Exception('%s is an unsupported or unknown language' % lang)

    model_names = get_spacy_models_for_language(lang)
    if model_name not in model_names:
        spacy.cli.download(model_name)

    # Load spacy model if not provided
    nlp = nlp or spacy.load(model_name, disable=['ner'])

    # Load language merger module (for merging edits)
    module_merger = import_module('errant.components.%s.merger' % lang)

    # Load language classifier module (for classifying edits)
    module_type_error_classifier = import_module(
        'errant.components.%s.classifier' % lang,
    )

    # The English classifier needs spacy
    if lang == 'en':
        module_type_error_classifier.nlp = nlp

    # Return a configured ERRANT annotator
    return Annotator(lang, nlp, module_merger, module_type_error_classifier)
