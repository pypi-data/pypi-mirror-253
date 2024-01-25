#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .list_properties import list_properties as list_properties_cls
from .cone_axis_vector_child import cone_axis_vector_child

class film_velocity(ListObject[cone_axis_vector_child]):
    """
    'film_velocity' child.
    """

    fluent_name = "film-velocity"

    command_names = \
        ['list_properties']

    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of film_velocity.
    """
    child_object_type: cone_axis_vector_child = cone_axis_vector_child
    """
    child_object_type of film_velocity.
    """
