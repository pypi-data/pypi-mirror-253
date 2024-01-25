#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .enabled_12 import enabled as enabled_cls
from .value_2 import value as value_cls
class joule_heat_parameter(Group):
    """
    'joule_heat_parameter' child.
    """

    fluent_name = "joule-heat-parameter"

    child_names = \
        ['enabled', 'value']

    enabled: enabled_cls = enabled_cls
    """
    enabled child of joule_heat_parameter.
    """
    value: value_cls = value_cls
    """
    value child of joule_heat_parameter.
    """
