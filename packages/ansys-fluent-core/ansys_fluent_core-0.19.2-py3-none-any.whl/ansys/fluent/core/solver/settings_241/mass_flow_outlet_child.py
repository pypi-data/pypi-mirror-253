#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .name import name as name_cls
from .phase_10 import phase as phase_cls
from .flow_direction import flow_direction as flow_direction_cls
from .direction_vector import direction_vector as direction_vector_cls
from .axis_direction_2 import axis_direction as axis_direction_cls
from .axis_origin_2 import axis_origin as axis_origin_cls
from .momentum_4 import momentum as momentum_cls
from .turbulence_3 import turbulence as turbulence_cls
from .thermal_3 import thermal as thermal_cls
from .radiation_3 import radiation as radiation_cls
from .species_8 import species as species_cls
from .dpm_1 import dpm as dpm_cls
from .multiphase_5 import multiphase as multiphase_cls
from .potential_2 import potential as potential_cls
from .structure_1 import structure as structure_cls
from .uds_1 import uds as uds_cls
from .icing_1 import icing as icing_cls
from .geometry_2 import geometry as geometry_cls
class mass_flow_outlet_child(Group):
    """
    'child_object_type' of mass_flow_outlet.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['name', 'phase', 'flow_direction', 'direction_vector',
         'axis_direction', 'axis_origin', 'momentum', 'turbulence', 'thermal',
         'radiation', 'species', 'dpm', 'multiphase', 'potential',
         'structure', 'uds', 'icing', 'geometry']

    name: name_cls = name_cls
    """
    name child of mass_flow_outlet_child.
    """
    phase: phase_cls = phase_cls
    """
    phase child of mass_flow_outlet_child.
    """
    flow_direction: flow_direction_cls = flow_direction_cls
    """
    flow_direction child of mass_flow_outlet_child.
    """
    direction_vector: direction_vector_cls = direction_vector_cls
    """
    direction_vector child of mass_flow_outlet_child.
    """
    axis_direction: axis_direction_cls = axis_direction_cls
    """
    axis_direction child of mass_flow_outlet_child.
    """
    axis_origin: axis_origin_cls = axis_origin_cls
    """
    axis_origin child of mass_flow_outlet_child.
    """
    momentum: momentum_cls = momentum_cls
    """
    momentum child of mass_flow_outlet_child.
    """
    turbulence: turbulence_cls = turbulence_cls
    """
    turbulence child of mass_flow_outlet_child.
    """
    thermal: thermal_cls = thermal_cls
    """
    thermal child of mass_flow_outlet_child.
    """
    radiation: radiation_cls = radiation_cls
    """
    radiation child of mass_flow_outlet_child.
    """
    species: species_cls = species_cls
    """
    species child of mass_flow_outlet_child.
    """
    dpm: dpm_cls = dpm_cls
    """
    dpm child of mass_flow_outlet_child.
    """
    multiphase: multiphase_cls = multiphase_cls
    """
    multiphase child of mass_flow_outlet_child.
    """
    potential: potential_cls = potential_cls
    """
    potential child of mass_flow_outlet_child.
    """
    structure: structure_cls = structure_cls
    """
    structure child of mass_flow_outlet_child.
    """
    uds: uds_cls = uds_cls
    """
    uds child of mass_flow_outlet_child.
    """
    icing: icing_cls = icing_cls
    """
    icing child of mass_flow_outlet_child.
    """
    geometry: geometry_cls = geometry_cls
    """
    geometry child of mass_flow_outlet_child.
    """
