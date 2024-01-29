# BearDataClass

![](README.assets/2024-01-28-00-09-10.png)

# Problem

A `dataframe` (in pandas or polars) often simply represents a collection of `dataclass` instances. However, we cannot access the new dataframe using dataclass attributes.

# Solution (How to use)

This package proposes the simple `BearDataClass` Mixin-class. Dataclasses inheriting from it come with a few convenience methods to operate on dataframes based on dataclasses:

```python
from dataclasses import dataclass
from beardataclass import BearDataClass

@dataclass
class Foo(BearDataClass):
    x: int

df = Foo.create_pandas_df([Foo(1), Foo(2)])
df.loc[:, Foo.fields().x] *= 2
recreated = Foo.from_row(df.iloc[0,:])
```

# How to install

Run `pip install BearDataClass`
