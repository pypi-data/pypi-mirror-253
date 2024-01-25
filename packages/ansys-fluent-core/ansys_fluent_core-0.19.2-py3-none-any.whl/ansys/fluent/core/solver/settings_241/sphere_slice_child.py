#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .name import name as name_cls
from .center import center as center_cls
from .radius import radius as radius_cls
from .display_3 import display as display_cls
class sphere_slice_child(Group):
    """
    'child_object_type' of sphere_slice.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['name', 'center', 'radius']

    name: name_cls = name_cls
    """
    name child of sphere_slice_child.
    """
    center: center_cls = center_cls
    """
    center child of sphere_slice_child.
    """
    radius: radius_cls = radius_cls
    """
    radius child of sphere_slice_child.
    """
    command_names = \
        ['display']

    display: display_cls = display_cls
    """
    display command of sphere_slice_child.
    """
