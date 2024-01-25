#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .control_time_step_size_variation import control_time_step_size_variation as control_time_step_size_variation_cls
from .use_average_cfl import use_average_cfl as use_average_cfl_cls
from .cfl_type import cfl_type as cfl_type_cls
class cfl_based_time_stepping_advanced_options(Group):
    """
    Advanced settings for CFL-based time stepping.
    """

    fluent_name = "cfl-based-time-stepping-advanced-options"

    child_names = \
        ['control_time_step_size_variation', 'use_average_cfl', 'cfl_type']

    control_time_step_size_variation: control_time_step_size_variation_cls = control_time_step_size_variation_cls
    """
    control_time_step_size_variation child of cfl_based_time_stepping_advanced_options.
    """
    use_average_cfl: use_average_cfl_cls = use_average_cfl_cls
    """
    use_average_cfl child of cfl_based_time_stepping_advanced_options.
    """
    cfl_type: cfl_type_cls = cfl_type_cls
    """
    cfl_type child of cfl_based_time_stepping_advanced_options.
    """
