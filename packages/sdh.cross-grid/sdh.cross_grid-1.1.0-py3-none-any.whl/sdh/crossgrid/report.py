from typing import Dict
from collections import OrderedDict

from .column import Column
from .row import ReportRow
from .types import (ObjT, RowKeyT, ColKeyT, HeaderT,
                    RowReduceCallbackT, ColReduceCallbackT, HeaderMapCallbackT,
                    RowMapCallbackT, AggCallbackT)


class CrossGridReport:
    def __init__(self, title: str,
                 row_reduce: RowReduceCallbackT,
                 row_map: RowMapCallbackT,
                 col_reduce: ColReduceCallbackT,
                 agg_function: AggCallbackT,
                 header_map: HeaderMapCallbackT,
                 *args, **kwargs):
        """
        row_reduce:   references to row reduce function
                      It takes element and should return row key

        row_map:      function to map row basic object;
                      takes 1 argument: object;
                      value, returned by this function, will be used when
                      printing row

        col_reduce:   same as row_reduce but for columns

        agg_function: function will be called on adding value to the column
                      for extracting data from object;
                      Takes 2 arguments: object, current value

        header_map: function will be called when adding new key into column header
                    Takes 1 argument: object

        """
        self.title = title

        # functions
        self.row_reduce = row_reduce
        self.row_map = row_map
        self.col_reduce = col_reduce
        self.agg_function = agg_function
        self.header_map = header_map

        # grid data
        self.row: Dict[RowKeyT, ReportRow] = OrderedDict()
        # columns definition
        self.columns: Dict[ColKeyT, HeaderT] = OrderedDict()

    def append(self, obj: ObjT):
        row_key = self.row_reduce(obj)
        col_key = self.col_reduce(obj)

        if col_key not in self.columns:
            self.columns[col_key] = self.header_map(obj)

        row_obj = self.row_map(obj)
        row = self.append_row(row_obj, row_key)
        row.append(col_key, obj)

    def append_row(self, row_obj: ReportRow, row_key: RowKeyT):
        return self.row.setdefault(row_key, ReportRow(self, row_obj, row_key))

    def append_column(self, col_obj: HeaderT, col_key: ColKeyT):
        self.columns.setdefault(col_key, col_obj)

    def iter_columns(self):
        return self.columns.values()

    def iter_columns_key(self):
        return self.columns.keys()

    def iter_rows(self):
        return self.row.values()

    def iter_column(self, col_key: ColKeyT):
        for row in self.row.values():
            yield row.columns.get(col_key) or Column(self, col_key)
