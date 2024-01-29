from typing import Dict
from .column import Column
from .types import RowT, RowKeyT, ColKeyT, ObjT


class ReportRow:
    def __init__(self, report, obj: RowT, row_key: RowKeyT):
        self.key = row_key
        self.report = report
        self.columns: Dict[ColKeyT, ObjT] = {}

        # will be used while rendering report as key object for row
        self.obj = obj
        if hasattr(self.obj, 'crossgrid_init'):
            _init = getattr(self.obj, 'crossgrid_init')
            if callable(_init):
                _init(self)

    def append(self, col_key: ColKeyT, obj: ObjT):
        col = self.columns.setdefault(col_key, Column(self, col_key))
        col.append(obj)

    def iter_columns(self):
        for col_key in self.report.columns.keys():
            yield self.columns.get(col_key) or Column(self, col_key)
