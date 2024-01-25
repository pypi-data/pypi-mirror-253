#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .method_7 import method as method_cls
from .static_injection import static_injection as static_injection_cls
class static_setup(Group):
    """
    'static_setup' child.
    """

    fluent_name = "static-setup"

    child_names = \
        ['method', 'static_injection']

    method: method_cls = method_cls
    """
    method child of static_setup.
    """
    static_injection: static_injection_cls = static_injection_cls
    """
    static_injection child of static_setup.
    """
