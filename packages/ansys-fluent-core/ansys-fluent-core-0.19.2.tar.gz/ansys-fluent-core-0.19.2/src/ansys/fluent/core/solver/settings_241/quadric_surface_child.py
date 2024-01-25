#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .name import name as name_cls
from .attribute import attribute as attribute_cls
from .value_1 import value as value_cls
from .display_3 import display as display_cls
class quadric_surface_child(Group):
    """
    'child_object_type' of quadric_surface.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['name', 'attribute', 'value']

    name: name_cls = name_cls
    """
    name child of quadric_surface_child.
    """
    attribute: attribute_cls = attribute_cls
    """
    attribute child of quadric_surface_child.
    """
    value: value_cls = value_cls
    """
    value child of quadric_surface_child.
    """
    command_names = \
        ['display']

    display: display_cls = display_cls
    """
    display command of quadric_surface_child.
    """
