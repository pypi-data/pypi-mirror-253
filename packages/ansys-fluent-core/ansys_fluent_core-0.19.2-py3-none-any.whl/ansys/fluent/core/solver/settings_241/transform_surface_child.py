#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .name import name as name_cls
from .surface_2 import surface as surface_cls
from .center_of_rotation import center_of_rotation as center_of_rotation_cls
from .angle_of_rotation import angle_of_rotation as angle_of_rotation_cls
from .translation_distance import translation_distance as translation_distance_cls
from .iso_distance import iso_distance as iso_distance_cls
from .display_3 import display as display_cls
class transform_surface_child(Group):
    """
    'child_object_type' of transform_surface.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['name', 'surface', 'center_of_rotation', 'angle_of_rotation',
         'translation_distance', 'iso_distance']

    name: name_cls = name_cls
    """
    name child of transform_surface_child.
    """
    surface: surface_cls = surface_cls
    """
    surface child of transform_surface_child.
    """
    center_of_rotation: center_of_rotation_cls = center_of_rotation_cls
    """
    center_of_rotation child of transform_surface_child.
    """
    angle_of_rotation: angle_of_rotation_cls = angle_of_rotation_cls
    """
    angle_of_rotation child of transform_surface_child.
    """
    translation_distance: translation_distance_cls = translation_distance_cls
    """
    translation_distance child of transform_surface_child.
    """
    iso_distance: iso_distance_cls = iso_distance_cls
    """
    iso_distance child of transform_surface_child.
    """
    command_names = \
        ['display']

    display: display_cls = display_cls
    """
    display command of transform_surface_child.
    """
