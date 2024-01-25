#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .name import name as name_cls
from .phase_5 import phase as phase_cls
from .momentum_1 import momentum as momentum_cls
from .turbulence_1 import turbulence as turbulence_cls
from .thermal_1 import thermal as thermal_cls
from .radiation_2 import radiation as radiation_cls
from .species_6 import species as species_cls
from .dpm import dpm as dpm_cls
from .multiphase_3 import multiphase as multiphase_cls
from .potential_1 import potential as potential_cls
from .structure_1 import structure as structure_cls
from .uds_1 import uds as uds_cls
from .icing_1 import icing as icing_cls
from .geometry_2 import geometry as geometry_cls
class inlet_vent_child(Group):
    """
    'child_object_type' of inlet_vent.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['name', 'phase', 'momentum', 'turbulence', 'thermal', 'radiation',
         'species', 'dpm', 'multiphase', 'potential', 'structure', 'uds',
         'icing', 'geometry']

    name: name_cls = name_cls
    """
    name child of inlet_vent_child.
    """
    phase: phase_cls = phase_cls
    """
    phase child of inlet_vent_child.
    """
    momentum: momentum_cls = momentum_cls
    """
    momentum child of inlet_vent_child.
    """
    turbulence: turbulence_cls = turbulence_cls
    """
    turbulence child of inlet_vent_child.
    """
    thermal: thermal_cls = thermal_cls
    """
    thermal child of inlet_vent_child.
    """
    radiation: radiation_cls = radiation_cls
    """
    radiation child of inlet_vent_child.
    """
    species: species_cls = species_cls
    """
    species child of inlet_vent_child.
    """
    dpm: dpm_cls = dpm_cls
    """
    dpm child of inlet_vent_child.
    """
    multiphase: multiphase_cls = multiphase_cls
    """
    multiphase child of inlet_vent_child.
    """
    potential: potential_cls = potential_cls
    """
    potential child of inlet_vent_child.
    """
    structure: structure_cls = structure_cls
    """
    structure child of inlet_vent_child.
    """
    uds: uds_cls = uds_cls
    """
    uds child of inlet_vent_child.
    """
    icing: icing_cls = icing_cls
    """
    icing child of inlet_vent_child.
    """
    geometry: geometry_cls = geometry_cls
    """
    geometry child of inlet_vent_child.
    """
