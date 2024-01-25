#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .enabled_12 import enabled as enabled_cls
from .calendar_time import calendar_time as calendar_time_cls
from .cycle_number import cycle_number as cycle_number_cls
from .operation_temperature import operation_temperature as operation_temperature_cls
from .calendar_life_params import calendar_life_params as calendar_life_params_cls
from .cycle_life_table import cycle_life_table as cycle_life_table_cls
class life_model(Group):
    """
    'life_model' child.
    """

    fluent_name = "life-model"

    child_names = \
        ['enabled', 'calendar_time', 'cycle_number', 'operation_temperature',
         'calendar_life_params', 'cycle_life_table']

    enabled: enabled_cls = enabled_cls
    """
    enabled child of life_model.
    """
    calendar_time: calendar_time_cls = calendar_time_cls
    """
    calendar_time child of life_model.
    """
    cycle_number: cycle_number_cls = cycle_number_cls
    """
    cycle_number child of life_model.
    """
    operation_temperature: operation_temperature_cls = operation_temperature_cls
    """
    operation_temperature child of life_model.
    """
    calendar_life_params: calendar_life_params_cls = calendar_life_params_cls
    """
    calendar_life_params child of life_model.
    """
    cycle_life_table: cycle_life_table_cls = cycle_life_table_cls
    """
    cycle_life_table child of life_model.
    """
