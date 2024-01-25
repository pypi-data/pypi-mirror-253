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
from .mom_center import mom_center as mom_center_cls
from .mom_axis import mom_axis as mom_axis_cls
from .reference_frame import reference_frame as reference_frame_cls
from .zones_2 import zones as zones_cls
from .per_zone import per_zone as per_zone_cls
from .average_over import average_over as average_over_cls
from .retain_instantaneous_values import retain_instantaneous_values as retain_instantaneous_values_cls
from .report_output_type import report_output_type as report_output_type_cls
from .physics_1 import physics as physics_cls
from .geometry_5 import geometry as geometry_cls
from .create_output_parameter import create_output_parameter as create_output_parameter_cls
class moment_child(Group):
    """
    'child_object_type' of moment.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['name', 'report_type', 'mom_center', 'mom_axis', 'reference_frame',
         'zones', 'per_zone', 'average_over', 'retain_instantaneous_values',
         'report_output_type', 'physics', 'geometry']

    name: name_cls = name_cls
    """
    name child of moment_child.
    """
    report_type: report_type_cls = report_type_cls
    """
    report_type child of moment_child.
    """
    mom_center: mom_center_cls = mom_center_cls
    """
    mom_center child of moment_child.
    """
    mom_axis: mom_axis_cls = mom_axis_cls
    """
    mom_axis child of moment_child.
    """
    reference_frame: reference_frame_cls = reference_frame_cls
    """
    reference_frame child of moment_child.
    """
    zones: zones_cls = zones_cls
    """
    zones child of moment_child.
    """
    per_zone: per_zone_cls = per_zone_cls
    """
    per_zone child of moment_child.
    """
    average_over: average_over_cls = average_over_cls
    """
    average_over child of moment_child.
    """
    retain_instantaneous_values: retain_instantaneous_values_cls = retain_instantaneous_values_cls
    """
    retain_instantaneous_values child of moment_child.
    """
    report_output_type: report_output_type_cls = report_output_type_cls
    """
    report_output_type child of moment_child.
    """
    physics: physics_cls = physics_cls
    """
    physics child of moment_child.
    """
    geometry: geometry_cls = geometry_cls
    """
    geometry child of moment_child.
    """
    command_names = \
        ['create_output_parameter']

    create_output_parameter: create_output_parameter_cls = create_output_parameter_cls
    """
    create_output_parameter command of moment_child.
    """
