#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .delete_1 import delete as delete_cls
from .list import list as list_cls
from .list_properties_1 import list_properties as list_properties_cls
from .make_a_copy import make_a_copy as make_a_copy_cls
from .display_frame import display_frame as display_frame_cls
from .hide_frame import hide_frame as hide_frame_cls
from .reference_frames_child import reference_frames_child

class reference_frames(NamedObject[reference_frames_child], _CreatableNamedObjectMixin[reference_frames_child]):
    """
    'reference_frames' child.
    """

    fluent_name = "reference-frames"

    command_names = \
        ['delete', 'list', 'list_properties', 'make_a_copy', 'display_frame',
         'hide_frame']

    delete: delete_cls = delete_cls
    """
    delete command of reference_frames.
    """
    list: list_cls = list_cls
    """
    list command of reference_frames.
    """
    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of reference_frames.
    """
    make_a_copy: make_a_copy_cls = make_a_copy_cls
    """
    make_a_copy command of reference_frames.
    """
    display_frame: display_frame_cls = display_frame_cls
    """
    display_frame command of reference_frames.
    """
    hide_frame: hide_frame_cls = hide_frame_cls
    """
    hide_frame command of reference_frames.
    """
    child_object_type: reference_frames_child = reference_frames_child
    """
    child_object_type of reference_frames.
    """
