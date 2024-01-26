from .core import NamedDataset
from typing import Literal, Callable


def load_dataset(name: str, split: Literal["test", "train"] = "test") -> NamedDataset:
    """Loads dataset. Downloads it to the local machine if necessary.

    Args:

    - name (str) - dataset name. Starts with hub prefix "hf:" (HuggingFace datasets hub),
        or "inno:" (Innodata datasets hub)

    - split (str) - split name

    Returns: Dataset
    """
    dataset_loader = _get_dataset_loader(name)
    return dataset_loader(name, split)


def _get_dataset_loader(name: str) -> Callable[[str, Literal["test", "train"]], NamedDataset]:
    if name.startswith("hf:"):
        from .hf.hf_dataset import HFDataset

        return HFDataset.load

    elif name.startswith("inno:"):
        from inno.inno_dataset import load_dataset as ld

        return ld

    else:
        raise ValueError(f"Unknown dataset hub: {name}")
