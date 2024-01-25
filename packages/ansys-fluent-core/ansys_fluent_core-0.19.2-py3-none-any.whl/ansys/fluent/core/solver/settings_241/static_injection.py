#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .list_properties import list_properties as list_properties_cls
from .static_injection_child import static_injection_child

class static_injection(ListObject[static_injection_child]):
    """
    'static_injection' child.
    """

    fluent_name = "static-injection"

    command_names = \
        ['list_properties']

    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of static_injection.
    """
    child_object_type: static_injection_child = static_injection_child
    """
    child_object_type of static_injection.
    """
