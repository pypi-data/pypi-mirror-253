#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .option_5 import option as option_cls
from .expert_1 import expert as expert_cls
from .hybrid import hybrid as hybrid_cls
class parallel(Group):
    """
    Main menu to allow users to set options controlling the parallel scheme used when tracking particles. 
    For more details please consult the help option of the corresponding menu or TUI command.
    """

    fluent_name = "parallel"

    child_names = \
        ['option', 'expert', 'hybrid']

    option: option_cls = option_cls
    """
    option child of parallel.
    """
    expert: expert_cls = expert_cls
    """
    expert child of parallel.
    """
    hybrid: hybrid_cls = hybrid_cls
    """
    hybrid child of parallel.
    """
