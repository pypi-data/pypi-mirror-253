from typing import Optional

from xprompt_common.api_schema.generate_schema import ParsingInfo
from xprompt_common.base_service import BaseService


class DummyParser(BaseService):
    val: str = ""

    def run(self) -> (str, Optional[ParsingInfo]):
        return self.val, None
