#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .delay_model_change_update import delay_model_change_update as delay_model_change_update_cls
from .batch_thread_update import batch_thread_update as batch_thread_update_cls
class advanced(Group):
    """
    Control settings while doing BC setup.
    """

    fluent_name = "advanced"

    child_names = \
        ['delay_model_change_update', 'batch_thread_update']

    delay_model_change_update: delay_model_change_update_cls = delay_model_change_update_cls
    """
    delay_model_change_update child of advanced.
    """
    batch_thread_update: batch_thread_update_cls = batch_thread_update_cls
    """
    batch_thread_update child of advanced.
    """
