#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .scheme_proc import scheme_proc as scheme_proc_cls
from .udf_side import udf_side as udf_side_cls
from .expression_2 import expression as expression_cls
from .list_4 import list as list_cls
class input_parameters(Group):
    """
    Enter the input-parameters menu.
    """

    fluent_name = "input-parameters"

    child_names = \
        ['scheme_proc', 'udf_side', 'expression']

    scheme_proc: scheme_proc_cls = scheme_proc_cls
    """
    scheme_proc child of input_parameters.
    """
    udf_side: udf_side_cls = udf_side_cls
    """
    udf_side child of input_parameters.
    """
    expression: expression_cls = expression_cls
    """
    expression child of input_parameters.
    """
    command_names = \
        ['list']

    list: list_cls = list_cls
    """
    list command of input_parameters.
    """
