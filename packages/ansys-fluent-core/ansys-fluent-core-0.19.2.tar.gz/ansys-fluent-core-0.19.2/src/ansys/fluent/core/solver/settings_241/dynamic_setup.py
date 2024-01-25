#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .method_6 import method as method_cls
from .dynamic_injection import dynamic_injection as dynamic_injection_cls
class dynamic_setup(Group):
    """
    'dynamic_setup' child.
    """

    fluent_name = "dynamic-setup"

    child_names = \
        ['method', 'dynamic_injection']

    method: method_cls = method_cls
    """
    method child of dynamic_setup.
    """
    dynamic_injection: dynamic_injection_cls = dynamic_injection_cls
    """
    dynamic_injection child of dynamic_setup.
    """
