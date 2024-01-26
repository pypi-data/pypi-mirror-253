from __future__ import annotations

from enum import Enum


class Language(Enum):
    ESP = "Spanish"
    ENG = "English"

    @staticmethod
    def get_language(abbreviation: str) -> Language:
        for lang in Language:
            if lang.name.lower() == abbreviation.lower():
                return lang
        raise NotImplementedError(f"{abbreviation} language not implemented yet")
