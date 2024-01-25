#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .verbosity_11 import verbosity as verbosity_cls
class options(Group):
    """
    Enter FAS multigrid options menu.
    """

    fluent_name = "options"

    child_names = \
        ['verbosity']

    verbosity: verbosity_cls = verbosity_cls
    """
    verbosity child of options.
    """
