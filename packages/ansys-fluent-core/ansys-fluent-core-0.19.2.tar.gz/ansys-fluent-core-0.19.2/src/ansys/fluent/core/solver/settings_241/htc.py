#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .calculation_method import calculation_method as calculation_method_cls
class htc(Group):
    """
    Enter the heat transfer coeficient menu.
    """

    fluent_name = "htc"

    child_names = \
        ['calculation_method']

    calculation_method: calculation_method_cls = calculation_method_cls
    """
    calculation_method child of htc.
    """
