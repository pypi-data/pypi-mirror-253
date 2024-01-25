#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .les_zone_1 import les_zone as les_zone_cls
from .udf_zmotion_name import udf_zmotion_name as udf_zmotion_name_cls
from .axis_origin_1 import axis_origin as axis_origin_cls
from .axis_direction_1 import axis_direction as axis_direction_cls
from .omega import omega as omega_cls
from .relative_to_thread import relative_to_thread as relative_to_thread_cls
from .motion_spec import motion_spec as motion_spec_cls
from .cylindrical_fixed_var import cylindrical_fixed_var as cylindrical_fixed_var_cls
class disabled(Group):
    """
    Help not available.
    """

    fluent_name = "disabled"

    child_names = \
        ['les_zone', 'udf_zmotion_name', 'axis_origin', 'axis_direction',
         'omega', 'relative_to_thread', 'motion_spec',
         'cylindrical_fixed_var']

    les_zone: les_zone_cls = les_zone_cls
    """
    les_zone child of disabled.
    """
    udf_zmotion_name: udf_zmotion_name_cls = udf_zmotion_name_cls
    """
    udf_zmotion_name child of disabled.
    """
    axis_origin: axis_origin_cls = axis_origin_cls
    """
    axis_origin child of disabled.
    """
    axis_direction: axis_direction_cls = axis_direction_cls
    """
    axis_direction child of disabled.
    """
    omega: omega_cls = omega_cls
    """
    omega child of disabled.
    """
    relative_to_thread: relative_to_thread_cls = relative_to_thread_cls
    """
    relative_to_thread child of disabled.
    """
    motion_spec: motion_spec_cls = motion_spec_cls
    """
    motion_spec child of disabled.
    """
    cylindrical_fixed_var: cylindrical_fixed_var_cls = cylindrical_fixed_var_cls
    """
    cylindrical_fixed_var child of disabled.
    """
