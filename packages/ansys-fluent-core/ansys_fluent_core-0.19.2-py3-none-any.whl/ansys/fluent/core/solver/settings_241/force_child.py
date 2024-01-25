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
from .force_vector import force_vector as force_vector_cls
from .reference_frame import reference_frame as reference_frame_cls
from .zones_2 import zones as zones_cls
from .per_zone import per_zone as per_zone_cls
from .average_over import average_over as average_over_cls
from .retain_instantaneous_values import retain_instantaneous_values as retain_instantaneous_values_cls
from .report_output_type import report_output_type as report_output_type_cls
from .physics_1 import physics as physics_cls
from .geometry_5 import geometry as geometry_cls
from .create_output_parameter import create_output_parameter as create_output_parameter_cls
class force_child(Group):
    """
    'child_object_type' of force.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['name', 'report_type', 'force_vector', 'reference_frame', 'zones',
         'per_zone', 'average_over', 'retain_instantaneous_values',
         'report_output_type', 'physics', 'geometry']

    name: name_cls = name_cls
    """
    name child of force_child.
    """
    report_type: report_type_cls = report_type_cls
    """
    report_type child of force_child.
    """
    force_vector: force_vector_cls = force_vector_cls
    """
    force_vector child of force_child.
    """
    reference_frame: reference_frame_cls = reference_frame_cls
    """
    reference_frame child of force_child.
    """
    zones: zones_cls = zones_cls
    """
    zones child of force_child.
    """
    per_zone: per_zone_cls = per_zone_cls
    """
    per_zone child of force_child.
    """
    average_over: average_over_cls = average_over_cls
    """
    average_over child of force_child.
    """
    retain_instantaneous_values: retain_instantaneous_values_cls = retain_instantaneous_values_cls
    """
    retain_instantaneous_values child of force_child.
    """
    report_output_type: report_output_type_cls = report_output_type_cls
    """
    report_output_type child of force_child.
    """
    physics: physics_cls = physics_cls
    """
    physics child of force_child.
    """
    geometry: geometry_cls = geometry_cls
    """
    geometry child of force_child.
    """
    command_names = \
        ['create_output_parameter']

    create_output_parameter: create_output_parameter_cls = create_output_parameter_cls
    """
    create_output_parameter command of force_child.
    """
