#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .enable_5 import enable as enable_cls
from .robustness_enhancement import robustness_enhancement as robustness_enhancement_cls
from .nasa9_enhancement import nasa9_enhancement as nasa9_enhancement_cls
from .set_verbosity import set_verbosity as set_verbosity_cls
from .translational_vibrational_energy_relaxation import translational_vibrational_energy_relaxation as translational_vibrational_energy_relaxation_cls
class two_temperature(Group):
    """
    Define two-temperature model menu.
    """

    fluent_name = "two-temperature"

    child_names = \
        ['enable', 'robustness_enhancement', 'nasa9_enhancement',
         'set_verbosity', 'translational_vibrational_energy_relaxation']

    enable: enable_cls = enable_cls
    """
    enable child of two_temperature.
    """
    robustness_enhancement: robustness_enhancement_cls = robustness_enhancement_cls
    """
    robustness_enhancement child of two_temperature.
    """
    nasa9_enhancement: nasa9_enhancement_cls = nasa9_enhancement_cls
    """
    nasa9_enhancement child of two_temperature.
    """
    set_verbosity: set_verbosity_cls = set_verbosity_cls
    """
    set_verbosity child of two_temperature.
    """
    translational_vibrational_energy_relaxation: translational_vibrational_energy_relaxation_cls = translational_vibrational_energy_relaxation_cls
    """
    translational_vibrational_energy_relaxation child of two_temperature.
    """
