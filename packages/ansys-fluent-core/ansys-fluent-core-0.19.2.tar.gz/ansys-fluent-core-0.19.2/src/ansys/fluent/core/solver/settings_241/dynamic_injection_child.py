#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .acd import acd as acd_cls
from .cd import cd as cd_cls
from .direction_2 import direction as direction_cls
from .angle_1 import angle as angle_cls
class dynamic_injection_child(Group):
    """
    'child_object_type' of dynamic_injection.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['acd', 'cd', 'direction', 'angle']

    acd: acd_cls = acd_cls
    """
    acd child of dynamic_injection_child.
    """
    cd: cd_cls = cd_cls
    """
    cd child of dynamic_injection_child.
    """
    direction: direction_cls = direction_cls
    """
    direction child of dynamic_injection_child.
    """
    angle: angle_cls = angle_cls
    """
    angle child of dynamic_injection_child.
    """
