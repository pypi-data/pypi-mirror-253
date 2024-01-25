#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .mesh_2 import mesh as mesh_cls
from .contour import contour as contour_cls
from .vector_1 import vector as vector_cls
from .pathline import pathline as pathline_cls
from .particle_track import particle_track as particle_track_cls
from .lic import lic as lic_cls
from .olic import olic as olic_cls
from .volumes_1 import volumes as volumes_cls
from .contours import contours as contours_cls
from .particle_tracks import particle_tracks as particle_tracks_cls
from .colors import colors as colors_cls
from .lighting import lighting as lighting_cls
from .picture import picture as picture_cls
from .views import views as views_cls
from .windows import windows as windows_cls
from .raytracing_options import raytracing_options as raytracing_options_cls
from .pulse import pulse as pulse_cls
class graphics(Group, _ChildNamedObjectAccessorMixin):
    """
    'graphics' child.
    """

    fluent_name = "graphics"

    child_names = \
        ['mesh', 'contour', 'vector', 'pathline', 'particle_track', 'lic',
         'olic', 'volumes', 'contours', 'particle_tracks', 'colors',
         'lighting', 'picture', 'views', 'windows', 'raytracing_options',
         'pulse']

    mesh: mesh_cls = mesh_cls
    """
    mesh child of graphics.
    """
    contour: contour_cls = contour_cls
    """
    contour child of graphics.
    """
    vector: vector_cls = vector_cls
    """
    vector child of graphics.
    """
    pathline: pathline_cls = pathline_cls
    """
    pathline child of graphics.
    """
    particle_track: particle_track_cls = particle_track_cls
    """
    particle_track child of graphics.
    """
    lic: lic_cls = lic_cls
    """
    lic child of graphics.
    """
    olic: olic_cls = olic_cls
    """
    olic child of graphics.
    """
    volumes: volumes_cls = volumes_cls
    """
    volumes child of graphics.
    """
    contours: contours_cls = contours_cls
    """
    contours child of graphics.
    """
    particle_tracks: particle_tracks_cls = particle_tracks_cls
    """
    particle_tracks child of graphics.
    """
    colors: colors_cls = colors_cls
    """
    colors child of graphics.
    """
    lighting: lighting_cls = lighting_cls
    """
    lighting child of graphics.
    """
    picture: picture_cls = picture_cls
    """
    picture child of graphics.
    """
    views: views_cls = views_cls
    """
    views child of graphics.
    """
    windows: windows_cls = windows_cls
    """
    windows child of graphics.
    """
    raytracing_options: raytracing_options_cls = raytracing_options_cls
    """
    raytracing_options child of graphics.
    """
    pulse: pulse_cls = pulse_cls
    """
    pulse child of graphics.
    """
