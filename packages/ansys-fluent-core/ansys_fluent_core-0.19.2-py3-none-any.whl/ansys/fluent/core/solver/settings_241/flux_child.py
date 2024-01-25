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
from .boundaries_1 import boundaries as boundaries_cls
from .per_zone import per_zone as per_zone_cls
from .average_over import average_over as average_over_cls
from .retain_instantaneous_values import retain_instantaneous_values as retain_instantaneous_values_cls
from .phase_26 import phase as phase_cls
from .physics_1 import physics as physics_cls
from .geometry_5 import geometry as geometry_cls
from .create_output_parameter import create_output_parameter as create_output_parameter_cls
class flux_child(Group):
    """
    'child_object_type' of flux.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['name', 'report_type', 'boundaries', 'per_zone', 'average_over',
         'retain_instantaneous_values', 'phase', 'physics', 'geometry']

    name: name_cls = name_cls
    """
    name child of flux_child.
    """
    report_type: report_type_cls = report_type_cls
    """
    report_type child of flux_child.
    """
    boundaries: boundaries_cls = boundaries_cls
    """
    boundaries child of flux_child.
    """
    per_zone: per_zone_cls = per_zone_cls
    """
    per_zone child of flux_child.
    """
    average_over: average_over_cls = average_over_cls
    """
    average_over child of flux_child.
    """
    retain_instantaneous_values: retain_instantaneous_values_cls = retain_instantaneous_values_cls
    """
    retain_instantaneous_values child of flux_child.
    """
    phase: phase_cls = phase_cls
    """
    phase child of flux_child.
    """
    physics: physics_cls = physics_cls
    """
    physics child of flux_child.
    """
    geometry: geometry_cls = geometry_cls
    """
    geometry child of flux_child.
    """
    command_names = \
        ['create_output_parameter']

    create_output_parameter: create_output_parameter_cls = create_output_parameter_cls
    """
    create_output_parameter command of flux_child.
    """
