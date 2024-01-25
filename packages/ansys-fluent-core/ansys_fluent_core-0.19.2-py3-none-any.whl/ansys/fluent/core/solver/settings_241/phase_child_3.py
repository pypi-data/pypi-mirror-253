#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .momentum import momentum as momentum_cls
from .turbulence import turbulence as turbulence_cls
from .thermal import thermal as thermal_cls
from .radiation_1 import radiation as radiation_cls
from .species_5 import species as species_cls
from .dpm import dpm as dpm_cls
from .multiphase_2 import multiphase as multiphase_cls
from .potential_1 import potential as potential_cls
from .structure_1 import structure as structure_cls
from .uds_1 import uds as uds_cls
from .icing import icing as icing_cls
from .geometry_2 import geometry as geometry_cls
class phase_child(Group):
    """
    'child_object_type' of phase.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['momentum', 'turbulence', 'thermal', 'radiation', 'species', 'dpm',
         'multiphase', 'potential', 'structure', 'uds', 'icing', 'geometry']

    momentum: momentum_cls = momentum_cls
    """
    momentum child of phase_child.
    """
    turbulence: turbulence_cls = turbulence_cls
    """
    turbulence child of phase_child.
    """
    thermal: thermal_cls = thermal_cls
    """
    thermal child of phase_child.
    """
    radiation: radiation_cls = radiation_cls
    """
    radiation child of phase_child.
    """
    species: species_cls = species_cls
    """
    species child of phase_child.
    """
    dpm: dpm_cls = dpm_cls
    """
    dpm child of phase_child.
    """
    multiphase: multiphase_cls = multiphase_cls
    """
    multiphase child of phase_child.
    """
    potential: potential_cls = potential_cls
    """
    potential child of phase_child.
    """
    structure: structure_cls = structure_cls
    """
    structure child of phase_child.
    """
    uds: uds_cls = uds_cls
    """
    uds child of phase_child.
    """
    icing: icing_cls = icing_cls
    """
    icing child of phase_child.
    """
    geometry: geometry_cls = geometry_cls
    """
    geometry child of phase_child.
    """
