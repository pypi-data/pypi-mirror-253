#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .ambient_color import ambient_color as ambient_color_cls
from .headlight_setting import headlight_setting as headlight_setting_cls
from .lights_on import lights_on as lights_on_cls
from .lighting_interpolation import lighting_interpolation as lighting_interpolation_cls
from .lights import lights as lights_cls
class lighting(Group):
    """
    'lighting' child.
    """

    fluent_name = "lighting"

    child_names = \
        ['ambient_color', 'headlight_setting', 'lights_on',
         'lighting_interpolation', 'lights']

    ambient_color: ambient_color_cls = ambient_color_cls
    """
    ambient_color child of lighting.
    """
    headlight_setting: headlight_setting_cls = headlight_setting_cls
    """
    headlight_setting child of lighting.
    """
    lights_on: lights_on_cls = lights_on_cls
    """
    lights_on child of lighting.
    """
    lighting_interpolation: lighting_interpolation_cls = lighting_interpolation_cls
    """
    lighting_interpolation child of lighting.
    """
    lights: lights_cls = lights_cls
    """
    lights child of lighting.
    """
