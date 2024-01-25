#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .option_8 import option as option_cls
from .value_4 import value as value_cls
from .profile_name import profile_name as profile_name_cls
from .field_name import field_name as field_name_cls
from .udf import udf as udf_cls
class log10_droplets_per_unit_volume(Group):
    """
    Log10(Droplets Per Unit Volume).
    """

    fluent_name = "log10-droplets-per-unit-volume"

    child_names = \
        ['option', 'value', 'profile_name', 'field_name', 'udf']

    option: option_cls = option_cls
    """
    option child of log10_droplets_per_unit_volume.
    """
    value: value_cls = value_cls
    """
    value child of log10_droplets_per_unit_volume.
    """
    profile_name: profile_name_cls = profile_name_cls
    """
    profile_name child of log10_droplets_per_unit_volume.
    """
    field_name: field_name_cls = field_name_cls
    """
    field_name child of log10_droplets_per_unit_volume.
    """
    udf: udf_cls = udf_cls
    """
    udf child of log10_droplets_per_unit_volume.
    """
