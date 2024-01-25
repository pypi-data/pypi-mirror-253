#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .on import on as on_cls
from .rgb import rgb as rgb_cls
from .direction_3 import direction as direction_cls
from .set_direction_from_view_vector import set_direction_from_view_vector as set_direction_from_view_vector_cls
class lights_child(Group):
    """
    'child_object_type' of lights.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['on', 'rgb', 'direction']

    on: on_cls = on_cls
    """
    on child of lights_child.
    """
    rgb: rgb_cls = rgb_cls
    """
    rgb child of lights_child.
    """
    direction: direction_cls = direction_cls
    """
    direction child of lights_child.
    """
    command_names = \
        ['set_direction_from_view_vector']

    set_direction_from_view_vector: set_direction_from_view_vector_cls = set_direction_from_view_vector_cls
    """
    set_direction_from_view_vector command of lights_child.
    """
