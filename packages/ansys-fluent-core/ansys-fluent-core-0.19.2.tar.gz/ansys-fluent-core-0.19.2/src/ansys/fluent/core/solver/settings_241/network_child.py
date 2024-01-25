#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .name import name as name_cls
from .phase_11 import phase as phase_cls
class network_child(Group):
    """
    'child_object_type' of network.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['name', 'phase']

    name: name_cls = name_cls
    """
    name child of network_child.
    """
    phase: phase_cls = phase_cls
    """
    phase child of network_child.
    """
