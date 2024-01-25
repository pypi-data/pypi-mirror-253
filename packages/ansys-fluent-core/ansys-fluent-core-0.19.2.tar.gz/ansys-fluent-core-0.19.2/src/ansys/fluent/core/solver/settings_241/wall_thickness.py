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
class wall_thickness(Group):
    """
    Wall Thickness.
    """

    fluent_name = "wall-thickness"

    child_names = \
        ['option', 'value', 'profile_name', 'field_name', 'udf']

    option: option_cls = option_cls
    """
    option child of wall_thickness.
    """
    value: value_cls = value_cls
    """
    value child of wall_thickness.
    """
    profile_name: profile_name_cls = profile_name_cls
    """
    profile_name child of wall_thickness.
    """
    field_name: field_name_cls = field_name_cls
    """
    field_name child of wall_thickness.
    """
    udf: udf_cls = udf_cls
    """
    udf child of wall_thickness.
    """
