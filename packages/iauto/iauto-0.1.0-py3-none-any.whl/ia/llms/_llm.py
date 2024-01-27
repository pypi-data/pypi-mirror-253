from abc import ABC, abstractmethod
from typing import List
from pydantic import BaseModel
from ..actions import Action


class Message(BaseModel):
    role: str
    content: str


class LLM(ABC):
    """LLM"""

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def generate(self, instructions: str, functions: List[Action] = None, **kwargs) -> Message:
        """"""

    @abstractmethod
    def chat(self, messages: List[Message], functions: List[Action] = None, **kwargs) -> Message:
        """"""
