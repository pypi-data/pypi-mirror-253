#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .type_2 import type as type_cls
from .minimum_1 import minimum as minimum_cls
from .maximum_1 import maximum as maximum_cls
class range_options(Group):
    """
    'range_options' child.
    """

    fluent_name = "range-options"

    child_names = \
        ['type', 'minimum', 'maximum']

    type: type_cls = type_cls
    """
    type child of range_options.
    """
    minimum: minimum_cls = minimum_cls
    """
    minimum child of range_options.
    """
    maximum: maximum_cls = maximum_cls
    """
    maximum child of range_options.
    """
