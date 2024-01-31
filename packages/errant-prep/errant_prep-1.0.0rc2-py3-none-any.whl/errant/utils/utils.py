from __future__ import annotations

import spacy


def get_available_spacy_models() -> list[str]:
    """
    Get a list of available spaCy models installed in the current environment.

    Returns:
        List[Text]: A list of available spaCy model names.
    """
    installed_models = spacy.info().get("pipelines", "")
    if not installed_models:
        return []
    return list(installed_models.keys())


def get_spacy_models_for_language(lang: str) -> list[str]:
    """
    Get a list of spaCy models that support a specific language.

    Args:
        lang (Text): The language code (e.g., 'en' for English) to filter models by.

    Returns:
        List[Text]: A list of spaCy model names that support the specified language.
    """
    installed_models = get_available_spacy_models()
    if not installed_models:
        return []

    return [
        model_name
        for model_name in installed_models
        if model_name.split("_")[0] == lang
    ]
