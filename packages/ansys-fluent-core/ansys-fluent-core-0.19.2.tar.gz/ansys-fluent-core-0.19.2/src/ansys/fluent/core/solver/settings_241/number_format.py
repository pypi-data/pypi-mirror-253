#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .format_type import format_type as format_type_cls
from .precision import precision as precision_cls
class number_format(Group):
    """
    Set number-formatting options.
    """

    fluent_name = "number-format"

    child_names = \
        ['format_type', 'precision']

    format_type: format_type_cls = format_type_cls
    """
    format_type child of number_format.
    """
    precision: precision_cls = precision_cls
    """
    precision child of number_format.
    """
