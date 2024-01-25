#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .blending_factor_1 import blending_factor as blending_factor_cls
from .bin_count import bin_count as bin_count_cls
class pressure_outlet(Group):
    """
    Select pressure specification method on pressure-outlet boundaries.
    """

    fluent_name = "pressure-outlet"

    child_names = \
        ['blending_factor', 'bin_count']

    blending_factor: blending_factor_cls = blending_factor_cls
    """
    blending_factor child of pressure_outlet.
    """
    bin_count: bin_count_cls = bin_count_cls
    """
    bin_count child of pressure_outlet.
    """
