#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .t import t as t_cls
from .thermodynamic_non_equilibrium_boundary import thermodynamic_non_equilibrium_boundary as thermodynamic_non_equilibrium_boundary_cls
from .vibrational_electronic_temperature import vibrational_electronic_temperature as vibrational_electronic_temperature_cls
class thermal(Group):
    """
    Help not available.
    """

    fluent_name = "thermal"

    child_names = \
        ['t', 'thermodynamic_non_equilibrium_boundary',
         'vibrational_electronic_temperature']

    t: t_cls = t_cls
    """
    t child of thermal.
    """
    thermodynamic_non_equilibrium_boundary: thermodynamic_non_equilibrium_boundary_cls = thermodynamic_non_equilibrium_boundary_cls
    """
    thermodynamic_non_equilibrium_boundary child of thermal.
    """
    vibrational_electronic_temperature: vibrational_electronic_temperature_cls = vibrational_electronic_temperature_cls
    """
    vibrational_electronic_temperature child of thermal.
    """
