#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .method_3 import method as method_cls
from .injection_hole import injection_hole as injection_hole_cls
class holes_setup(Group):
    """
    'holes_setup' child.
    """

    fluent_name = "holes-setup"

    child_names = \
        ['method', 'injection_hole']

    method: method_cls = method_cls
    """
    method child of holes_setup.
    """
    injection_hole: injection_hole_cls = injection_hole_cls
    """
    injection_hole child of holes_setup.
    """
