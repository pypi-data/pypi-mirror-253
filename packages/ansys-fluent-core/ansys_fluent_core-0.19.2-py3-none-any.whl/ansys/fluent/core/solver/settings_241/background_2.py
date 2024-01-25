#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .hide_environment_keep_effects import hide_environment_keep_effects as hide_environment_keep_effects_cls
from .environment_image import environment_image as environment_image_cls
from .vertical import vertical as vertical_cls
from .horizontal import horizontal as horizontal_cls
from .spin import spin as spin_cls
from .env_color import env_color as env_color_cls
from .env_intensity import env_intensity as env_intensity_cls
from .view_zoom import view_zoom as view_zoom_cls
from .show_backplate import show_backplate as show_backplate_cls
from .backplate_color import backplate_color as backplate_color_cls
from .backplate_image import backplate_image as backplate_image_cls
from .env_light_upvec import env_light_upvec as env_light_upvec_cls
from .env_light_dirvec import env_light_dirvec as env_light_dirvec_cls
class background(Group):
    """
    Enter the menu for background options.
    """

    fluent_name = "background"

    child_names = \
        ['hide_environment_keep_effects', 'environment_image', 'vertical',
         'horizontal', 'spin', 'env_color', 'env_intensity', 'view_zoom',
         'show_backplate', 'backplate_color', 'backplate_image',
         'env_light_upvec', 'env_light_dirvec']

    hide_environment_keep_effects: hide_environment_keep_effects_cls = hide_environment_keep_effects_cls
    """
    hide_environment_keep_effects child of background.
    """
    environment_image: environment_image_cls = environment_image_cls
    """
    environment_image child of background.
    """
    vertical: vertical_cls = vertical_cls
    """
    vertical child of background.
    """
    horizontal: horizontal_cls = horizontal_cls
    """
    horizontal child of background.
    """
    spin: spin_cls = spin_cls
    """
    spin child of background.
    """
    env_color: env_color_cls = env_color_cls
    """
    env_color child of background.
    """
    env_intensity: env_intensity_cls = env_intensity_cls
    """
    env_intensity child of background.
    """
    view_zoom: view_zoom_cls = view_zoom_cls
    """
    view_zoom child of background.
    """
    show_backplate: show_backplate_cls = show_backplate_cls
    """
    show_backplate child of background.
    """
    backplate_color: backplate_color_cls = backplate_color_cls
    """
    backplate_color child of background.
    """
    backplate_image: backplate_image_cls = backplate_image_cls
    """
    backplate_image child of background.
    """
    env_light_upvec: env_light_upvec_cls = env_light_upvec_cls
    """
    env_light_upvec child of background.
    """
    env_light_dirvec: env_light_dirvec_cls = env_light_dirvec_cls
    """
    env_light_dirvec child of background.
    """
