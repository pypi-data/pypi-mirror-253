#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .playback import playback as playback_cls
from .scene_animation import scene_animation as scene_animation_cls
class animations(Group):
    """
    'animations' child.
    """

    fluent_name = "animations"

    child_names = \
        ['playback', 'scene_animation']

    playback: playback_cls = playback_cls
    """
    playback child of animations.
    """
    scene_animation: scene_animation_cls = scene_animation_cls
    """
    scene_animation child of animations.
    """
