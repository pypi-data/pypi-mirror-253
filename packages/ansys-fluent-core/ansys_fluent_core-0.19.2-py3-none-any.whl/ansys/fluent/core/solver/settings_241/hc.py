#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .option import option as option_cls
from .function_of import function_of as function_of_cls
from .value_4 import value as value_cls
from .piecewise_polynomial import piecewise_polynomial as piecewise_polynomial_cls
from .piecewise_linear_1 import piecewise_linear as piecewise_linear_cls
from .polynomial_1 import polynomial as polynomial_cls
class hc(Group):
    """
    Heat-Transfer-Coefficient.
    """

    fluent_name = "hc"

    child_names = \
        ['option', 'function_of', 'value', 'piecewise_polynomial',
         'piecewise_linear', 'polynomial']

    option: option_cls = option_cls
    """
    option child of hc.
    """
    function_of: function_of_cls = function_of_cls
    """
    function_of child of hc.
    """
    value: value_cls = value_cls
    """
    value child of hc.
    """
    piecewise_polynomial: piecewise_polynomial_cls = piecewise_polynomial_cls
    """
    piecewise_polynomial child of hc.
    """
    piecewise_linear: piecewise_linear_cls = piecewise_linear_cls
    """
    piecewise_linear child of hc.
    """
    polynomial: polynomial_cls = polynomial_cls
    """
    polynomial child of hc.
    """
