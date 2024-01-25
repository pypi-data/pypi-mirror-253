#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .name import name as name_cls
from .motion import motion as motion_cls
from .parent_1 import parent_1 as parent_1_cls
from .initial_state import initial_state as initial_state_cls
from .display_state import display_state as display_state_cls
class reference_frames_child(Group):
    """
    'child_object_type' of reference_frames.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['name', 'motion', 'parent_1', 'initial_state', 'display_state']

    name: name_cls = name_cls
    """
    name child of reference_frames_child.
    """
    motion: motion_cls = motion_cls
    """
    motion child of reference_frames_child.
    """
    parent_1: parent_1_cls = parent_1_cls
    """
    parent_1 child of reference_frames_child.
    """
    initial_state: initial_state_cls = initial_state_cls
    """
    initial_state child of reference_frames_child.
    """
    display_state: display_state_cls = display_state_cls
    """
    display_state child of reference_frames_child.
    """
