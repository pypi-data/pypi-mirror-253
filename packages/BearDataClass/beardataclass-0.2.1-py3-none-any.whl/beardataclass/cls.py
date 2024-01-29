from __future__ import annotations

import dataclasses
from typing import TYPE_CHECKING, ClassVar, Protocol, TypeVar

if TYPE_CHECKING:
    from collections.abc import Iterable

import pandas as pd


# See https://stackoverflow.com/a/55240861/2135504
class IsDataclass(Protocol):
    __dataclass_fields__: ClassVar[dict]


T = TypeVar("T", bound="BearDataClass")


@dataclasses.dataclass
class BearDataClass:
    @classmethod
    def fields(cls: type[T]) -> T:
        # TODO: How to deal with init=False fields?
        # We can exclude them, but then repr error...
        dct = {f.name: f.name for f in dataclasses.fields(cls)}
        return cls(**dct)

    @classmethod
    def create_pandas_df(cls: type[T], items: Iterable[IsDataclass]) -> pd.DataFrame:
        return pd.DataFrame.from_records(
            data=(dataclasses.asdict(i) for i in items),
            columns=[f.name for f in dataclasses.fields(cls)],
        )

    @classmethod
    def from_row(cls: type[T], row: pd.Series) -> T:
        return cls(**row)
