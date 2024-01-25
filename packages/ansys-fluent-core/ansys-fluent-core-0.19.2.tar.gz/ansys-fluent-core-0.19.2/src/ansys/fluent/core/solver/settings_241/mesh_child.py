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
from .per_zone import per_zone as per_zone_cls
from .average_over import average_over as average_over_cls
from .retain_instantaneous_values import retain_instantaneous_values as retain_instantaneous_values_cls
from .cell_zones_3 import cell_zones as cell_zones_cls
from .face_zones import face_zones as face_zones_cls
from .create_output_parameter import create_output_parameter as create_output_parameter_cls
class mesh_child(Group):
    """
    'child_object_type' of mesh.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['name', 'report_type', 'per_zone', 'average_over',
         'retain_instantaneous_values', 'cell_zones', 'face_zones']

    name: name_cls = name_cls
    """
    name child of mesh_child.
    """
    report_type: report_type_cls = report_type_cls
    """
    report_type child of mesh_child.
    """
    per_zone: per_zone_cls = per_zone_cls
    """
    per_zone child of mesh_child.
    """
    average_over: average_over_cls = average_over_cls
    """
    average_over child of mesh_child.
    """
    retain_instantaneous_values: retain_instantaneous_values_cls = retain_instantaneous_values_cls
    """
    retain_instantaneous_values child of mesh_child.
    """
    cell_zones: cell_zones_cls = cell_zones_cls
    """
    cell_zones child of mesh_child.
    """
    face_zones: face_zones_cls = face_zones_cls
    """
    face_zones child of mesh_child.
    """
    command_names = \
        ['create_output_parameter']

    create_output_parameter: create_output_parameter_cls = create_output_parameter_cls
    """
    create_output_parameter command of mesh_child.
    """
