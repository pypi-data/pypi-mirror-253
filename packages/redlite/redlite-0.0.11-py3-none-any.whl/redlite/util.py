import hashlib
import json
import os
from collections.abc import Iterable, Iterator, Sized
from .core import NamedDataset, DatasetItem, ScoreSummary

__all__ = [
    "DatasetRunningDigest",
    "parse_duration",
    "format_duration",
    "redlite_data_dir",
]
__docformat__ = "google"


def _serialize(obj: dict | DatasetItem) -> bytes:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True).encode("utf-8")


class DatasetRunningDigest(Sized, Iterable[DatasetItem]):
    def __init__(self, dataset: NamedDataset, **kw):
        self._hash = hashlib.sha256(usedforsecurity=False)
        self._hash.update(_serialize(kw))
        self._dataset = dataset

    def __iter__(self) -> Iterator[DatasetItem]:
        for item in self._dataset:
            yield item
            self._hash.update(_serialize(item))

    def __len__(self):
        return len(self._dataset)

    @property
    def hexdigest(self) -> str:
        return self._hash.hexdigest()


def format_duration(seconds: float) -> str:
    """Formats duration to a compact human-readable string, e.g. "1d 4h 27m 14.5s" """
    out = []
    minutes = seconds // 60
    seconds -= minutes * 60
    out.append(f"{round(seconds, 2)}s")
    if minutes > 0:
        hours = minutes // 60
        minutes -= hours * 60
        out.append(f"{minutes}m")
        if hours > 0:
            days = hours // 24
            hours -= days * 24
            out.append(f"{hours}h")
            if days > 0:
                out.append(f"{days}d")
    return " ".join(reversed(out))


def parse_duration(duration: str) -> float:
    """Parses human-readable duration into float number, representing seconds"""
    seconds = 0.0
    minutes = 0
    hours = 0
    days = 0
    for x in reversed(duration.split()):
        if x[-1] == "s":
            seconds = float(x[:-1])
        elif x[-1] == "m":
            minutes = int(x[:-1])
        elif x[-1] == "h":
            hours = int(x[:-1])
        elif x[-1] == "d":
            days = int(x[:-1])
        else:
            raise ValueError(f"Invalid duration string: [{duration}]")
    return seconds + minutes * 60 + hours * 60 * 60 + days * 24 * 60 * 60


def redlite_data_dir() -> str:
    """Returns the location of RedLite data directory"""
    return os.environ.get("REDLITE_DATA_DIR", os.path.expanduser("~/.cache/redlite"))


class ScoreAccumulator:
    def __init__(self):
        self._min = 100000  # FIXME?
        self._max = 0.0
        self._acc = 0.0
        self._count = 0

    def __call__(self, score: float) -> None:
        self._acc += score
        self._min = min(self._min, score)
        self._max = max(self._max, score)
        self._count += 1

    @property
    def summary(self) -> ScoreSummary:
        mean = 0.0 if self._count == 0 else self._acc / self._count
        return dict(
            count=self._count,
            mean=mean,
            min=self._min,
            max=self._max,
        )
