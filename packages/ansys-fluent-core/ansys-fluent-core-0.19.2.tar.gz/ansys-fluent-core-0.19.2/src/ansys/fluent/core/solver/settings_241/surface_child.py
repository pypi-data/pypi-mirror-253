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
from .surface_names import surface_names as surface_names_cls
from .per_surface import per_surface as per_surface_cls
from .average_over import average_over as average_over_cls
from .retain_instantaneous_values import retain_instantaneous_values as retain_instantaneous_values_cls
from .custom_vector import custom_vector as custom_vector_cls
from .phase_26 import phase as phase_cls
from .physics_1 import physics as physics_cls
from .geometry_5 import geometry as geometry_cls
from .surfaces_2 import surfaces as surfaces_cls
from .create_output_parameter import create_output_parameter as create_output_parameter_cls
class surface_child(Group):
    """
    'child_object_type' of surface.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['name', 'report_type', 'field', 'surface_names', 'per_surface',
         'average_over', 'retain_instantaneous_values', 'custom_vector',
         'phase', 'physics', 'geometry', 'surfaces']

    name: name_cls = name_cls
    """
    name child of surface_child.
    """
    report_type: report_type_cls = report_type_cls
    """
    report_type child of surface_child.
    """
    field: field_cls = field_cls
    """
    field child of surface_child.
    """
    surface_names: surface_names_cls = surface_names_cls
    """
    surface_names child of surface_child.
    """
    per_surface: per_surface_cls = per_surface_cls
    """
    per_surface child of surface_child.
    """
    average_over: average_over_cls = average_over_cls
    """
    average_over child of surface_child.
    """
    retain_instantaneous_values: retain_instantaneous_values_cls = retain_instantaneous_values_cls
    """
    retain_instantaneous_values child of surface_child.
    """
    custom_vector: custom_vector_cls = custom_vector_cls
    """
    custom_vector child of surface_child.
    """
    phase: phase_cls = phase_cls
    """
    phase child of surface_child.
    """
    physics: physics_cls = physics_cls
    """
    physics child of surface_child.
    """
    geometry: geometry_cls = geometry_cls
    """
    geometry child of surface_child.
    """
    surfaces: surfaces_cls = surfaces_cls
    """
    surfaces child of surface_child.
    """
    command_names = \
        ['create_output_parameter']

    create_output_parameter: create_output_parameter_cls = create_output_parameter_cls
    """
    create_output_parameter command of surface_child.
    """
