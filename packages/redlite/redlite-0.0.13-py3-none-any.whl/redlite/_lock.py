import contextlib
import os
import json
from collections.abc import Iterator

__all__ = ["incr_run_count"]


@contextlib.contextmanager
def file_lock(fname: str) -> Iterator[None]:
    lockfile = fname + ".lock"
    try:
        os.open(lockfile, os.O_CREAT | os.O_EXCL | os.O_RDWR)
        yield
    finally:
        os.unlink(lockfile)


def incr_run_count() -> int:
    fname = os.path.expanduser("~/.cache/redlite/count.json")
    os.makedirs(os.path.dirname(fname), exist_ok=True)
    with file_lock(fname):
        if not os.path.isfile(fname):
            count = 0
        else:
            with open(fname, "r", encoding="utf-8") as f:
                count = json.load(f)

        count += 1
        with open(fname, "w", encoding="utf-8") as f:
            json.dump(count, f)
    return count
