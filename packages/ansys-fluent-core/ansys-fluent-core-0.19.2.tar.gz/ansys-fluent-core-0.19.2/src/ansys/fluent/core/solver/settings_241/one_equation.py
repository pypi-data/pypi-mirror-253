#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .data_type import data_type as data_type_cls
from .hw import hw as hw_cls
from .a import a as a_cls
from .e import e as e_cls
from .m import m as m_cls
from .n import n as n_cls
from .alpha0 import alpha0 as alpha0_cls
from .rate_table import rate_table as rate_table_cls
from .hw_table import hw_table as hw_table_cls
from .hw_udf import hw_udf as hw_udf_cls
from .udf_name import udf_name as udf_name_cls
class one_equation(Group):
    """
    'one_equation' child.
    """

    fluent_name = "one-equation"

    child_names = \
        ['data_type', 'hw', 'a', 'e', 'm', 'n', 'alpha0', 'rate_table',
         'hw_table', 'hw_udf', 'udf_name']

    data_type: data_type_cls = data_type_cls
    """
    data_type child of one_equation.
    """
    hw: hw_cls = hw_cls
    """
    hw child of one_equation.
    """
    a: a_cls = a_cls
    """
    a child of one_equation.
    """
    e: e_cls = e_cls
    """
    e child of one_equation.
    """
    m: m_cls = m_cls
    """
    m child of one_equation.
    """
    n: n_cls = n_cls
    """
    n child of one_equation.
    """
    alpha0: alpha0_cls = alpha0_cls
    """
    alpha0 child of one_equation.
    """
    rate_table: rate_table_cls = rate_table_cls
    """
    rate_table child of one_equation.
    """
    hw_table: hw_table_cls = hw_table_cls
    """
    hw_table child of one_equation.
    """
    hw_udf: hw_udf_cls = hw_udf_cls
    """
    hw_udf child of one_equation.
    """
    udf_name: udf_name_cls = udf_name_cls
    """
    udf_name child of one_equation.
    """
