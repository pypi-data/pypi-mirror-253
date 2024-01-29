CrossGrid Report Engine
=====================

The ``CrossGridReport`` class is designed for creating pivot table-like reports in Python. 
It offers flexibility through custom callback functions for row and column processing, data aggregation, 
and header mapping.


Class Initialization
--------------------

```python
CrossGridReport(title: str,
                row_reduce: RowReduceCallbackT,
                row_map: RowMapCallbackT,
                col_reduce: ColReduceCallbackT,
                agg_function: AggCallbackT,
                header_map: HeaderMapCallbackT,
                *args, **kwargs)
```


Parameters
---------

- **title** (*str*): The title of the report.
- **row_reduce** (*RowReduceCallbackT*): Callback for row reduction.
- **row_map** (*RowMapCallbackT*): Callback for mapping row data.
- **col_reduce** (*ColReduceCallbackT*): Callback for column reduction.
- **agg_function** (*AggCallbackT*): Callback for data aggregation in columns.
- **header_map** (*HeaderMapCallbackT*): Callback for mapping column headers.


Usage
-----

To utilize the ``CrossGridReport`` class, define the required callback functions based on data processing needs. These functions will guide the processing of rows and columns, data aggregation, and header mapping. Instantiate the class with these functions to create a customized pivot table report.


Define and populate data
------------------------


```python
from django.db import models
from sdh.crossgrid import CrossGridReport


class OrderItem(models.Model):
    name = models.CharField()

    
class Orders(models.Model):
    item = models.ForeignKey(OrderItem)
    sales_date = models.DateField()
    amount = models.DecimalField()

    
def row_reduce(obj):
    return obj.item.id

def row_map(obj):
    return obj.item

def col_reduce(obj):
    return obj.sales_date

def agg_function(obj, current_val):
    return (obj or Decimal('0')) + current_val

def header_map(obj):
    return str(obj.sales_date)


qs = Orders.objects.all()

report = CrossGridReport("Sales by items",
                         row_reduce=row_reduce,
                         row_map=row_map,
                         col_reduce=col_reduce,
                         agg_function=agg_function,
                         header_map=header_map)

for obj in qs:
    report.append(obj)

```


Render data as HTML
------------------------

Example below shows how to render report with Django template

```html
<table>
    <thead>
      <tr>
        <th>Order item</th>
        {% for column in report.iter_columns %}
            <!-- it will be str(date) -->
            <th>{{ column }}</th>
        {% endfor %}  
      </tr>
    </thead>
    <tbody>
      {% for row in report.iter_rows %}
        <tr>
            <th>{{ row.obj.name }} <!-- this is OrderItem.name --></th>
            {% for col in row.iter_columns %}
              <th>{{ col }} <!-- this is result of agg_function --></th>
            {% endfor %}
        </tr>
      {% endfor %}
    </tbody>
```
