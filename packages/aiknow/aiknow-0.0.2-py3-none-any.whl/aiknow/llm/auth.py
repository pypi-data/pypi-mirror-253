from typing import Self
from abc import ABC, abstractclassmethod
from pydantic_settings import BaseSettings


class LLMAuth(BaseSettings, ABC):
    pass
    # @abstractclassmethod
    # def from_env(cls) -> Self:
    #     pass
