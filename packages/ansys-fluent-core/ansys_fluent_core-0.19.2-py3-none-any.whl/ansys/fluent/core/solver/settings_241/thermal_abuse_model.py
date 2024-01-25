#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .enabled_12 import enabled as enabled_cls
from .model_type import model_type as model_type_cls
from .only_abuse import only_abuse as only_abuse_cls
from .one_equation import one_equation as one_equation_cls
from .four_equation import four_equation as four_equation_cls
from .internal_short import internal_short as internal_short_cls
class thermal_abuse_model(Group):
    """
    'thermal_abuse_model' child.
    """

    fluent_name = "thermal-abuse-model"

    child_names = \
        ['enabled', 'model_type', 'only_abuse', 'one_equation',
         'four_equation', 'internal_short']

    enabled: enabled_cls = enabled_cls
    """
    enabled child of thermal_abuse_model.
    """
    model_type: model_type_cls = model_type_cls
    """
    model_type child of thermal_abuse_model.
    """
    only_abuse: only_abuse_cls = only_abuse_cls
    """
    only_abuse child of thermal_abuse_model.
    """
    one_equation: one_equation_cls = one_equation_cls
    """
    one_equation child of thermal_abuse_model.
    """
    four_equation: four_equation_cls = four_equation_cls
    """
    four_equation child of thermal_abuse_model.
    """
    internal_short: internal_short_cls = internal_short_cls
    """
    internal_short child of thermal_abuse_model.
    """
