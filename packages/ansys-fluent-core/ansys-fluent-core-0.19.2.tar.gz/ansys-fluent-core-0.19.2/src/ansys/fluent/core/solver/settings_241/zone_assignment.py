#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .positive_electrode_zone import positive_electrode_zone as positive_electrode_zone_cls
from .electrolyte_zone import electrolyte_zone as electrolyte_zone_cls
from .negative_electrode_zone import negative_electrode_zone as negative_electrode_zone_cls
class zone_assignment(Group):
    """
    'zone_assignment' child.
    """

    fluent_name = "zone-assignment"

    child_names = \
        ['positive_electrode_zone', 'electrolyte_zone',
         'negative_electrode_zone']

    positive_electrode_zone: positive_electrode_zone_cls = positive_electrode_zone_cls
    """
    positive_electrode_zone child of zone_assignment.
    """
    electrolyte_zone: electrolyte_zone_cls = electrolyte_zone_cls
    """
    electrolyte_zone child of zone_assignment.
    """
    negative_electrode_zone: negative_electrode_zone_cls = negative_electrode_zone_cls
    """
    negative_electrode_zone child of zone_assignment.
    """
