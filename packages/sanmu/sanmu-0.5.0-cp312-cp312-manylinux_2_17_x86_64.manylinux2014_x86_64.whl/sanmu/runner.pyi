from _typeshed import Incomplete
from enum import IntEnum
from pytest_xlsx.file import XlsxItem as XlsxItem
from sanmu import settings as settings
from typing import Any

logger: Incomplete

class ScreenshotType(IntEnum):
    STEP: int
    ERROR: int

class Step:
    name: str
    key_word: str
    args: list
    @classmethod
    def from_case(cls, step: dict[str, Any]): ...
    def __attrs_post_init__(self) -> None: ...

class SanmuRunner:
    kw: Incomplete
    case_screenshot_list: Incomplete
    has_alert: bool
    def __init__(self, exchanger, usefixtures) -> None: ...
    def execute(self, item: XlsxItem): ...
    def save_screenshot(self, name, type) -> None: ...
    def save_gif(self) -> None: ...
