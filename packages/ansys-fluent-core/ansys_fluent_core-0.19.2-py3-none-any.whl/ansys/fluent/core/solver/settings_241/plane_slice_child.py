#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .name import name as name_cls
from .normal import normal as normal_cls
from .distance_from_origin import distance_from_origin as distance_from_origin_cls
from .display_3 import display as display_cls
class plane_slice_child(Group):
    """
    'child_object_type' of plane_slice.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['name', 'normal', 'distance_from_origin']

    name: name_cls = name_cls
    """
    name child of plane_slice_child.
    """
    normal: normal_cls = normal_cls
    """
    normal child of plane_slice_child.
    """
    distance_from_origin: distance_from_origin_cls = distance_from_origin_cls
    """
    distance_from_origin child of plane_slice_child.
    """
    command_names = \
        ['display']

    display: display_cls = display_cls
    """
    display command of plane_slice_child.
    """
