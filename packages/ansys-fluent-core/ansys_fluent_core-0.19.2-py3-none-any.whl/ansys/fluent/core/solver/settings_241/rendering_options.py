#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .animation_option import animation_option as animation_option_cls
from .auto_spin import auto_spin as auto_spin_cls
from .color_map_alignment import color_map_alignment as color_map_alignment_cls
from .double_buffering import double_buffering as double_buffering_cls
from .face_displacement import face_displacement as face_displacement_cls
from .hidden_surface_method import hidden_surface_method as hidden_surface_method_cls
from .hidden_surfaces import hidden_surfaces as hidden_surfaces_cls
from .front_faces_transparent_1 import front_faces_transparent as front_faces_transparent_cls
from .show_colormap import show_colormap as show_colormap_cls
from .device_info import device_info as device_info_cls
from .driver import driver as driver_cls
from .set_rendering_options import set_rendering_options as set_rendering_options_cls
class rendering_options(Group):
    """
    'rendering_options' child.
    """

    fluent_name = "rendering-options"

    child_names = \
        ['animation_option', 'auto_spin', 'color_map_alignment',
         'double_buffering', 'face_displacement', 'hidden_surface_method',
         'hidden_surfaces', 'front_faces_transparent', 'show_colormap']

    animation_option: animation_option_cls = animation_option_cls
    """
    animation_option child of rendering_options.
    """
    auto_spin: auto_spin_cls = auto_spin_cls
    """
    auto_spin child of rendering_options.
    """
    color_map_alignment: color_map_alignment_cls = color_map_alignment_cls
    """
    color_map_alignment child of rendering_options.
    """
    double_buffering: double_buffering_cls = double_buffering_cls
    """
    double_buffering child of rendering_options.
    """
    face_displacement: face_displacement_cls = face_displacement_cls
    """
    face_displacement child of rendering_options.
    """
    hidden_surface_method: hidden_surface_method_cls = hidden_surface_method_cls
    """
    hidden_surface_method child of rendering_options.
    """
    hidden_surfaces: hidden_surfaces_cls = hidden_surfaces_cls
    """
    hidden_surfaces child of rendering_options.
    """
    front_faces_transparent: front_faces_transparent_cls = front_faces_transparent_cls
    """
    front_faces_transparent child of rendering_options.
    """
    show_colormap: show_colormap_cls = show_colormap_cls
    """
    show_colormap child of rendering_options.
    """
    command_names = \
        ['device_info', 'driver', 'set_rendering_options']

    device_info: device_info_cls = device_info_cls
    """
    device_info command of rendering_options.
    """
    driver: driver_cls = driver_cls
    """
    driver command of rendering_options.
    """
    set_rendering_options: set_rendering_options_cls = set_rendering_options_cls
    """
    set_rendering_options command of rendering_options.
    """
