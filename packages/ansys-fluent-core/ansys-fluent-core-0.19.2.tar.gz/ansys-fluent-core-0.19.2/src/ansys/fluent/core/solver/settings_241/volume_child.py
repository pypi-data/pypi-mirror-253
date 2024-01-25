#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .name import name as name_cls
from .report_type import report_type as report_type_cls
from .field import field as field_cls
from .cell_zones_4 import cell_zones as cell_zones_cls
from .per_zone import per_zone as per_zone_cls
from .average_over import average_over as average_over_cls
from .retain_instantaneous_values import retain_instantaneous_values as retain_instantaneous_values_cls
from .phase_26 import phase as phase_cls
from .physics_1 import physics as physics_cls
from .geometry_5 import geometry as geometry_cls
from .create_output_parameter import create_output_parameter as create_output_parameter_cls
class volume_child(Group):
    """
    'child_object_type' of volume.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['name', 'report_type', 'field', 'cell_zones', 'per_zone',
         'average_over', 'retain_instantaneous_values', 'phase', 'physics',
         'geometry']

    name: name_cls = name_cls
    """
    name child of volume_child.
    """
    report_type: report_type_cls = report_type_cls
    """
    report_type child of volume_child.
    """
    field: field_cls = field_cls
    """
    field child of volume_child.
    """
    cell_zones: cell_zones_cls = cell_zones_cls
    """
    cell_zones child of volume_child.
    """
    per_zone: per_zone_cls = per_zone_cls
    """
    per_zone child of volume_child.
    """
    average_over: average_over_cls = average_over_cls
    """
    average_over child of volume_child.
    """
    retain_instantaneous_values: retain_instantaneous_values_cls = retain_instantaneous_values_cls
    """
    retain_instantaneous_values child of volume_child.
    """
    phase: phase_cls = phase_cls
    """
    phase child of volume_child.
    """
    physics: physics_cls = physics_cls
    """
    physics child of volume_child.
    """
    geometry: geometry_cls = geometry_cls
    """
    geometry child of volume_child.
    """
    command_names = \
        ['create_output_parameter']

    create_output_parameter: create_output_parameter_cls = create_output_parameter_cls
    """
    create_output_parameter command of volume_child.
    """
