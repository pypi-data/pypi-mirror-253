#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .set_custom_frames import set_custom_frames as set_custom_frames_cls
from .video_1 import video as video_cls
from .current_animation import current_animation as current_animation_cls
from .read_animation_file import read_animation_file as read_animation_file_cls
from .write_animation import write_animation as write_animation_cls
from .stored_view import stored_view as stored_view_cls
from .delete_5 import delete as delete_cls
from .play import play as play_cls
class playback(Group):
    """
    'playback' child.
    """

    fluent_name = "playback"

    child_names = \
        ['set_custom_frames', 'video', 'current_animation']

    set_custom_frames: set_custom_frames_cls = set_custom_frames_cls
    """
    set_custom_frames child of playback.
    """
    video: video_cls = video_cls
    """
    video child of playback.
    """
    current_animation: current_animation_cls = current_animation_cls
    """
    current_animation child of playback.
    """
    command_names = \
        ['read_animation_file', 'write_animation', 'stored_view', 'delete',
         'play']

    read_animation_file: read_animation_file_cls = read_animation_file_cls
    """
    read_animation_file command of playback.
    """
    write_animation: write_animation_cls = write_animation_cls
    """
    write_animation command of playback.
    """
    stored_view: stored_view_cls = stored_view_cls
    """
    stored_view command of playback.
    """
    delete: delete_cls = delete_cls
    """
    delete command of playback.
    """
    play: play_cls = play_cls
    """
    play command of playback.
    """
