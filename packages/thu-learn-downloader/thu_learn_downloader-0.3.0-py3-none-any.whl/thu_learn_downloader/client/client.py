from collections.abc import Mapping
from enum import StrEnum
from typing import Any, Optional

from requests import Response, Session

MAX_SIZE: int = 200


class Language(StrEnum):
    ENGLISH = "en"
    CHINESE = "zh"


class Client(Session):
    language: Language

    def __init__(self, language: Language = Language.ENGLISH, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.language = language

    def get_with_token(
        self, url: str, params: Optional[Mapping[str, Any]] = None
    ) -> Response:
        params = params or {}
        return self.get(url=url, params={**params, "_csrf": self.token})

    @property
    def token(self) -> None:
        return self.cookies["XSRF-TOKEN"]
