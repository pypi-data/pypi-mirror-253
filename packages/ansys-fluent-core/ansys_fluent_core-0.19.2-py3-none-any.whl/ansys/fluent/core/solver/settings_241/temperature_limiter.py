#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .leidenfrost_temp_postproc_enabled import leidenfrost_temp_postproc_enabled as leidenfrost_temp_postproc_enabled_cls
from .enabled_10 import enabled as enabled_cls
from .temp_limit_rel_to_boil_point import temp_limit_rel_to_boil_point as temp_limit_rel_to_boil_point_cls
class temperature_limiter(Group):
    """
    'temperature_limiter' child.
    """

    fluent_name = "temperature-limiter"

    child_names = \
        ['leidenfrost_temp_postproc_enabled', 'enabled',
         'temp_limit_rel_to_boil_point']

    leidenfrost_temp_postproc_enabled: leidenfrost_temp_postproc_enabled_cls = leidenfrost_temp_postproc_enabled_cls
    """
    leidenfrost_temp_postproc_enabled child of temperature_limiter.
    """
    enabled: enabled_cls = enabled_cls
    """
    enabled child of temperature_limiter.
    """
    temp_limit_rel_to_boil_point: temp_limit_rel_to_boil_point_cls = temp_limit_rel_to_boil_point_cls
    """
    temp_limit_rel_to_boil_point child of temperature_limiter.
    """
