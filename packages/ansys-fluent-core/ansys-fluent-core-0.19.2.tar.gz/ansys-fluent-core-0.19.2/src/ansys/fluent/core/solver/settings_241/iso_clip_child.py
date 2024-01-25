#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .name import name as name_cls
from .field_1 import field as field_cls
from .surfaces_4 import surfaces as surfaces_cls
from .min_3 import min as min_cls
from .max_3 import max as max_cls
from .display_3 import display as display_cls
class iso_clip_child(Group):
    """
    'child_object_type' of iso_clip.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['name', 'field', 'surfaces', 'min', 'max']

    name: name_cls = name_cls
    """
    name child of iso_clip_child.
    """
    field: field_cls = field_cls
    """
    field child of iso_clip_child.
    """
    surfaces: surfaces_cls = surfaces_cls
    """
    surfaces child of iso_clip_child.
    """
    min: min_cls = min_cls
    """
    min child of iso_clip_child.
    """
    max: max_cls = max_cls
    """
    max child of iso_clip_child.
    """
    command_names = \
        ['display']

    display: display_cls = display_cls
    """
    display command of iso_clip_child.
    """
