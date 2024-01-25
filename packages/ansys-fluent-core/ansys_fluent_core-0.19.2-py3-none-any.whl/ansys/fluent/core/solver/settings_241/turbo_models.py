#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .enable_turbo_model import enable_turbo_model as enable_turbo_model_cls
from .general_turbo_interface_settings import general_turbo_interface_settings as general_turbo_interface_settings_cls
class turbo_models(Group):
    """
    Enter the turbo-models settings.
    """

    fluent_name = "turbo-models"

    child_names = \
        ['enable_turbo_model', 'general_turbo_interface_settings']

    enable_turbo_model: enable_turbo_model_cls = enable_turbo_model_cls
    """
    enable_turbo_model child of turbo_models.
    """
    general_turbo_interface_settings: general_turbo_interface_settings_cls = general_turbo_interface_settings_cls
    """
    general_turbo_interface_settings child of turbo_models.
    """
