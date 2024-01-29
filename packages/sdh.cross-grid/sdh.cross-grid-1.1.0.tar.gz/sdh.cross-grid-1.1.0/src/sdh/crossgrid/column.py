from typing import Optional
from .types import ObjT


class Column:
    def __init__(self, report_row, key):
        self.key = key
        self.report_row = report_row
        self.value: Optional[ObjT] = None

    def append(self, obj: ObjT):
        self.value = self.report_row.report.agg_function(obj, self.value)
