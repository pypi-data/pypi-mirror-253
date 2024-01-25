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
from .zones_2 import zones as zones_cls
from .per_zone import per_zone as per_zone_cls
from .nodal_diameters import nodal_diameters as nodal_diameters_cls
from .average_over import average_over as average_over_cls
from .integrate_over import integrate_over as integrate_over_cls
from .normalization import normalization as normalization_cls
from .realcomponent import realcomponent as realcomponent_cls
from .create_output_parameter import create_output_parameter as create_output_parameter_cls
class aeromechanics_child(Group):
    """
    'child_object_type' of aeromechanics.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['name', 'report_type', 'zones', 'per_zone', 'nodal_diameters',
         'average_over', 'integrate_over', 'normalization', 'realcomponent']

    name: name_cls = name_cls
    """
    name child of aeromechanics_child.
    """
    report_type: report_type_cls = report_type_cls
    """
    report_type child of aeromechanics_child.
    """
    zones: zones_cls = zones_cls
    """
    zones child of aeromechanics_child.
    """
    per_zone: per_zone_cls = per_zone_cls
    """
    per_zone child of aeromechanics_child.
    """
    nodal_diameters: nodal_diameters_cls = nodal_diameters_cls
    """
    nodal_diameters child of aeromechanics_child.
    """
    average_over: average_over_cls = average_over_cls
    """
    average_over child of aeromechanics_child.
    """
    integrate_over: integrate_over_cls = integrate_over_cls
    """
    integrate_over child of aeromechanics_child.
    """
    normalization: normalization_cls = normalization_cls
    """
    normalization child of aeromechanics_child.
    """
    realcomponent: realcomponent_cls = realcomponent_cls
    """
    realcomponent child of aeromechanics_child.
    """
    command_names = \
        ['create_output_parameter']

    create_output_parameter: create_output_parameter_cls = create_output_parameter_cls
    """
    create_output_parameter command of aeromechanics_child.
    """
