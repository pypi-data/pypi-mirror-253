#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .option_4 import option as option_cls
from .gaussian_factor import gaussian_factor as gaussian_factor_cls
class kernel(Group):
    """
    'kernel' child.
    """

    fluent_name = "kernel"

    child_names = \
        ['option', 'gaussian_factor']

    option: option_cls = option_cls
    """
    option child of kernel.
    """
    gaussian_factor: gaussian_factor_cls = gaussian_factor_cls
    """
    gaussian_factor child of kernel.
    """
