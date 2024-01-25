#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .entropic_heat_enabled import entropic_heat_enabled as entropic_heat_enabled_cls
from .data_type_1 import data_type as data_type_cls
from .two_tables import two_tables as two_tables_cls
from .table_discharge import table_discharge as table_discharge_cls
from .table_charge import table_charge as table_charge_cls
from .udf_name import udf_name as udf_name_cls
class entropic_heat(Group):
    """
    'entropic_heat' child.
    """

    fluent_name = "entropic-heat"

    child_names = \
        ['entropic_heat_enabled', 'data_type', 'two_tables',
         'table_discharge', 'table_charge', 'udf_name']

    entropic_heat_enabled: entropic_heat_enabled_cls = entropic_heat_enabled_cls
    """
    entropic_heat_enabled child of entropic_heat.
    """
    data_type: data_type_cls = data_type_cls
    """
    data_type child of entropic_heat.
    """
    two_tables: two_tables_cls = two_tables_cls
    """
    two_tables child of entropic_heat.
    """
    table_discharge: table_discharge_cls = table_discharge_cls
    """
    table_discharge child of entropic_heat.
    """
    table_charge: table_charge_cls = table_charge_cls
    """
    table_charge child of entropic_heat.
    """
    udf_name: udf_name_cls = udf_name_cls
    """
    udf_name child of entropic_heat.
    """
