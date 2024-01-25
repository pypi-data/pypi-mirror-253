#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .method_4 import method as method_cls
from .value_1 import value as value_cls
from .user_defined import user_defined as user_defined_cls
class anode_ocv(Group):
    """
    'anode_ocv' child.
    """

    fluent_name = "anode-ocv"

    child_names = \
        ['method', 'value', 'user_defined']

    method: method_cls = method_cls
    """
    method child of anode_ocv.
    """
    value: value_cls = value_cls
    """
    value child of anode_ocv.
    """
    user_defined: user_defined_cls = user_defined_cls
    """
    user_defined child of anode_ocv.
    """
