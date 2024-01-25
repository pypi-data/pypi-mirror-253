#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .name import name as name_cls
from .phase_6 import phase as phase_cls
from .momentum_2 import momentum as momentum_cls
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
class intake_fan_child(Group):
    """
    'child_object_type' of intake_fan.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['name', 'phase', 'momentum', 'turbulence', 'thermal', 'radiation',
         'species', 'dpm', 'multiphase', 'potential', 'structure', 'uds',
         'icing', 'geometry']

    name: name_cls = name_cls
    """
    name child of intake_fan_child.
    """
    phase: phase_cls = phase_cls
    """
    phase child of intake_fan_child.
    """
    momentum: momentum_cls = momentum_cls
    """
    momentum child of intake_fan_child.
    """
    turbulence: turbulence_cls = turbulence_cls
    """
    turbulence child of intake_fan_child.
    """
    thermal: thermal_cls = thermal_cls
    """
    thermal child of intake_fan_child.
    """
    radiation: radiation_cls = radiation_cls
    """
    radiation child of intake_fan_child.
    """
    species: species_cls = species_cls
    """
    species child of intake_fan_child.
    """
    dpm: dpm_cls = dpm_cls
    """
    dpm child of intake_fan_child.
    """
    multiphase: multiphase_cls = multiphase_cls
    """
    multiphase child of intake_fan_child.
    """
    potential: potential_cls = potential_cls
    """
    potential child of intake_fan_child.
    """
    structure: structure_cls = structure_cls
    """
    structure child of intake_fan_child.
    """
    uds: uds_cls = uds_cls
    """
    uds child of intake_fan_child.
    """
    icing: icing_cls = icing_cls
    """
    icing child of intake_fan_child.
    """
    geometry: geometry_cls = geometry_cls
    """
    geometry child of intake_fan_child.
    """
