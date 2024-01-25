#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .list_properties import list_properties as list_properties_cls
from .injection_hole_child import injection_hole_child

class injection_hole(ListObject[injection_hole_child]):
    """
    'injection_hole' child.
    """

    fluent_name = "injection-hole"

    command_names = \
        ['list_properties']

    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of injection_hole.
    """
    child_object_type: injection_hole_child = injection_hole_child
    """
    child_object_type of injection_hole.
    """
