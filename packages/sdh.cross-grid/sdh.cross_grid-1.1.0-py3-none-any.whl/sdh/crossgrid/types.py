from typing import Callable, TypeVar

ObjT = TypeVar("ObjT")
HeaderT = TypeVar("HeaderT")
RowKeyT = TypeVar("RowKeyT")
ColKeyT = TypeVar("ColKeyT")
RowT = TypeVar("RowT")

RowReduceCallbackT = Callable[[ObjT], RowKeyT]
ColReduceCallbackT = Callable[[ObjT], ColKeyT]
HeaderMapCallbackT = Callable[[ObjT], HeaderT]
RowMapCallbackT = Callable[[ObjT], RowT]
AggCallbackT = Callable[[ObjT], ObjT]
