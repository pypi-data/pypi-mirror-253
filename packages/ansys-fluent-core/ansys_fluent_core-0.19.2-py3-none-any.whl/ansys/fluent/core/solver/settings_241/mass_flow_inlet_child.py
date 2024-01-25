#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .name import name as name_cls
from .phase_9 import phase as phase_cls
from .momentum_3 import momentum as momentum_cls
from .turbulence_2 import turbulence as turbulence_cls
from .thermal_2 import thermal as thermal_cls
from .radiation_3 import radiation as radiation_cls
from .species_7 import species as species_cls
from .dpm_1 import dpm as dpm_cls
from .multiphase_4 import multiphase as multiphase_cls
from .potential_1 import potential as potential_cls
from .structure_1 import structure as structure_cls
from .uds_1 import uds as uds_cls
from .icing_1 import icing as icing_cls
from .geometry_2 import geometry as geometry_cls
class mass_flow_inlet_child(Group):
    """
    'child_object_type' of mass_flow_inlet.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['name', 'phase', 'momentum', 'turbulence', 'thermal', 'radiation',
         'species', 'dpm', 'multiphase', 'potential', 'structure', 'uds',
         'icing', 'geometry']

    name: name_cls = name_cls
    """
    name child of mass_flow_inlet_child.
    """
    phase: phase_cls = phase_cls
    """
    phase child of mass_flow_inlet_child.
    """
    momentum: momentum_cls = momentum_cls
    """
    momentum child of mass_flow_inlet_child.
    """
    turbulence: turbulence_cls = turbulence_cls
    """
    turbulence child of mass_flow_inlet_child.
    """
    thermal: thermal_cls = thermal_cls
    """
    thermal child of mass_flow_inlet_child.
    """
    radiation: radiation_cls = radiation_cls
    """
    radiation child of mass_flow_inlet_child.
    """
    species: species_cls = species_cls
    """
    species child of mass_flow_inlet_child.
    """
    dpm: dpm_cls = dpm_cls
    """
    dpm child of mass_flow_inlet_child.
    """
    multiphase: multiphase_cls = multiphase_cls
    """
    multiphase child of mass_flow_inlet_child.
    """
    potential: potential_cls = potential_cls
    """
    potential child of mass_flow_inlet_child.
    """
    structure: structure_cls = structure_cls
    """
    structure child of mass_flow_inlet_child.
    """
    uds: uds_cls = uds_cls
    """
    uds child of mass_flow_inlet_child.
    """
    icing: icing_cls = icing_cls
    """
    icing child of mass_flow_inlet_child.
    """
    geometry: geometry_cls = geometry_cls
    """
    geometry child of mass_flow_inlet_child.
    """
