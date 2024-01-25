#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .start_keyframe import start_keyframe as start_keyframe_cls
from .end_keyframe import end_keyframe as end_keyframe_cls
from .increment_2 import increment as increment_cls
class set_custom_frames(Group):
    """
    Set custom frames start, end, skip frames for video export.
    """

    fluent_name = "set-custom-frames"

    child_names = \
        ['start_keyframe', 'end_keyframe', 'increment']

    start_keyframe: start_keyframe_cls = start_keyframe_cls
    """
    start_keyframe child of set_custom_frames.
    """
    end_keyframe: end_keyframe_cls = end_keyframe_cls
    """
    end_keyframe child of set_custom_frames.
    """
    increment: increment_cls = increment_cls
    """
    increment child of set_custom_frames.
    """
