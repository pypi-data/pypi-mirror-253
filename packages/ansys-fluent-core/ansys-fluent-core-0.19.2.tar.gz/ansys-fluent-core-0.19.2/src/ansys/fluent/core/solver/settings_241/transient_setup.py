#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .time_stepping_method import time_stepping_method as time_stepping_method_cls
from .max_time import max_time as max_time_cls
from .dt_0 import dt_0 as dt_0_cls
from .dt_max import dt_max as dt_max_cls
from .increment_factor import increment_factor as increment_factor_cls
from .n_time_step_per_setting import n_time_step_per_setting as n_time_step_per_setting_cls
from .max_n_per_time_step import max_n_per_time_step as max_n_per_time_step_cls
from .file_name import file_name as file_name_cls
from .stop_range_fraction import stop_range_fraction as stop_range_fraction_cls
class transient_setup(Group):
    """
    'transient_setup' child.
    """

    fluent_name = "transient-setup"

    child_names = \
        ['time_stepping_method', 'max_time', 'dt_0', 'dt_max',
         'increment_factor', 'n_time_step_per_setting', 'max_n_per_time_step',
         'file_name', 'stop_range_fraction']

    time_stepping_method: time_stepping_method_cls = time_stepping_method_cls
    """
    time_stepping_method child of transient_setup.
    """
    max_time: max_time_cls = max_time_cls
    """
    max_time child of transient_setup.
    """
    dt_0: dt_0_cls = dt_0_cls
    """
    dt_0 child of transient_setup.
    """
    dt_max: dt_max_cls = dt_max_cls
    """
    dt_max child of transient_setup.
    """
    increment_factor: increment_factor_cls = increment_factor_cls
    """
    increment_factor child of transient_setup.
    """
    n_time_step_per_setting: n_time_step_per_setting_cls = n_time_step_per_setting_cls
    """
    n_time_step_per_setting child of transient_setup.
    """
    max_n_per_time_step: max_n_per_time_step_cls = max_n_per_time_step_cls
    """
    max_n_per_time_step child of transient_setup.
    """
    file_name: file_name_cls = file_name_cls
    """
    file_name child of transient_setup.
    """
    stop_range_fraction: stop_range_fraction_cls = stop_range_fraction_cls
    """
    stop_range_fraction child of transient_setup.
    """
