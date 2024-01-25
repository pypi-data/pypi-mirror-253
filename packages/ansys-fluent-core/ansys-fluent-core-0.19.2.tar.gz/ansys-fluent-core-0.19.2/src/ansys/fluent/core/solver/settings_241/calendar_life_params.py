#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .ref_temperature import ref_temperature as ref_temperature_cls
from .pre_exp_fac import pre_exp_fac as pre_exp_fac_cls
from .activation_e import activation_e as activation_e_cls
from .exponent_value import exponent_value as exponent_value_cls
class calendar_life_params(Group):
    """
    'calendar_life_params' child.
    """

    fluent_name = "calendar-life-params"

    child_names = \
        ['ref_temperature', 'pre_exp_fac', 'activation_e', 'exponent_value']

    ref_temperature: ref_temperature_cls = ref_temperature_cls
    """
    ref_temperature child of calendar_life_params.
    """
    pre_exp_fac: pre_exp_fac_cls = pre_exp_fac_cls
    """
    pre_exp_fac child of calendar_life_params.
    """
    activation_e: activation_e_cls = activation_e_cls
    """
    activation_e child of calendar_life_params.
    """
    exponent_value: exponent_value_cls = exponent_value_cls
    """
    exponent_value child of calendar_life_params.
    """
