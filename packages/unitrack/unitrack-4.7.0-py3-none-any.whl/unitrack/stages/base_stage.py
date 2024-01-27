from abc import abstractmethod
from typing import Iterable, List, Tuple

import torch
from tensordict import TensorDictBase

__all__ = ["Stage"]


class Stage(torch.nn.Module):
    """
    Base class for stages in a ::class::`..Tracker`.

    Inputs to a stage are in the context data, or as fields of the detections.
    """

    def __init__(
        self,
        required_fields: Iterable[str] = (),
    ):
        super().__init__()

        self.required_fields = list(required_fields)

    def __repr__(self) -> str:
        req = ", ".join(self.required_fields)
        return f"{type(self).__name__}(fields=[{req}])"

    @abstractmethod
    def forward(
        self,
        ctx: TensorDictBase,
        cs: TensorDictBase,
        ds: TensorDictBase,
    ) -> Tuple[TensorDictBase, TensorDictBase]:
        raise NotImplementedError
