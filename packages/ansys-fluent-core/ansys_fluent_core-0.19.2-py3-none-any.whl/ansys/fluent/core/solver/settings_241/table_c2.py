#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .row_number import row_number as row_number_cls
from .column_number import column_number as column_number_cls
from .row_value import row_value as row_value_cls
from .column_value import column_value as column_value_cls
from .table_value import table_value as table_value_cls
class table_c2(Group):
    """
    'table_c2' child.
    """

    fluent_name = "table-c2"

    child_names = \
        ['row_number', 'column_number', 'row_value', 'column_value',
         'table_value']

    row_number: row_number_cls = row_number_cls
    """
    row_number child of table_c2.
    """
    column_number: column_number_cls = column_number_cls
    """
    column_number child of table_c2.
    """
    row_value: row_value_cls = row_value_cls
    """
    row_value child of table_c2.
    """
    column_value: column_value_cls = column_value_cls
    """
    column_value child of table_c2.
    """
    table_value: table_value_cls = table_value_cls
    """
    table_value child of table_c2.
    """
