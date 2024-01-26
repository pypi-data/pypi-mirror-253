import dataclasses
import abc
from collections.abc import Callable, Iterable, Sized
from typing import TypedDict, Literal
import logging


log = logging.getLogger("redlite")


Role = Literal["system", "user", "assistant"]
"""Type for the message role"""

Message = TypedDict("Message", {"role": Role, "content": str})
"""Message has content and role"""

Messages = list[Message]
"""Messages is just a list of ... messages!"""

Batch = list[Messages]
"""Messages can be batched for faster evaluation (i.e. on a GPU)"""

DatasetItem = TypedDict("DatasetItem", {"id": str, "messages": Messages, "expected": str})
"""Unique id, sessages, and the expected completion"""

Split = Literal["test", "train"]
"""Type for the dataset split"""


def system_message(content: str) -> Message:
    return {"role": "system", "content": content}


def user_message(content: str) -> Message:
    return {"role": "user", "content": content}


def assistant_message(content: str) -> Message:
    return {"role": "assistant", "content": content}


class NamedDataset(Sized, Iterable[DatasetItem]):
    name: str
    labels: dict[str, str]
    split: Split


class NamedMetric:
    name: str

    def __init__(self, name: str, engine: Callable[[str, str], float]):
        self.name = name
        self.engine = engine

    def __call__(self, expected: str, actual: str) -> float:
        return self.engine(expected, actual)


class NamedModel:
    name: str

    def __init__(self, name: str, engine: Callable[[Messages], str]):
        self.name = name
        self.engine = engine

    def __call__(self, conversation: Messages) -> str:
        return self.engine(conversation)


class Storage(abc.ABC):
    def __init__(self, name: str):
        self.name = name

    @abc.abstractmethod
    def save(self, item: DatasetItem, response: str, score: float):
        pass

    @abc.abstractmethod
    def save_meta(self, **kw):
        pass


@dataclasses.dataclass
class Experiment:
    """Represents experiment run"""

    name: str


class MissingDependencyError(RuntimeError):
    """Raised when a missing optional dependency is detected"""


ScoreSummary = TypedDict("ScoreSummary", {"count": int, "mean": float, "min": float, "max": float})
