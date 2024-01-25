#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .list_properties import list_properties as list_properties_cls
from .thin_wall_child import thin_wall_child

class thin_wall(ListObject[thin_wall_child]):
    """
    Layer.
    """

    fluent_name = "thin-wall"

    command_names = \
        ['list_properties']

    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of thin_wall.
    """
    child_object_type: thin_wall_child = thin_wall_child
    """
    child_object_type of thin_wall.
    """
