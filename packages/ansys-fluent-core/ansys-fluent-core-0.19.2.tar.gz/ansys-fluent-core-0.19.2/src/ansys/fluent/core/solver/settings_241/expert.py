#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .list_properties import list_properties as list_properties_cls
from .list_all import list_all as list_all_cls
from .expert_child import expert_child

class expert(ListObject[expert_child]):
    """
    Expert options in Park's model.
    """

    fluent_name = "expert"

    command_names = \
        ['list_properties', 'list_all']

    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of expert.
    """
    list_all: list_all_cls = list_all_cls
    """
    list_all command of expert.
    """
    child_object_type: expert_child = expert_child
    """
    child_object_type of expert.
    """
