#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .list_properties import list_properties as list_properties_cls
from .dynamic_injection_child import dynamic_injection_child

class dynamic_injection(ListObject[dynamic_injection_child]):
    """
    'dynamic_injection' child.
    """

    fluent_name = "dynamic-injection"

    command_names = \
        ['list_properties']

    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of dynamic_injection.
    """
    child_object_type: dynamic_injection_child = dynamic_injection_child
    """
    child_object_type of dynamic_injection.
    """
