from abc import abstractmethod
from typing import Optional

from bs4 import Tag
from pydantic import BaseModel

from xprompt_common.api_schema.generate_schema import ParsingInfo


class BaseService(BaseModel):
    @classmethod
    def create_from_tag(cls, tag: Tag, **user_info):
        """create class based on bs4 tag and user info"""
        creation_dict = tag.attrs
        creation_dict.update(**user_info)
        if tag.text:
            creation_dict["text"] = tag.text

        return cls(**creation_dict)

    @abstractmethod
    def run(self) -> (str, Optional[ParsingInfo]):
        """replace the tag with string"""
