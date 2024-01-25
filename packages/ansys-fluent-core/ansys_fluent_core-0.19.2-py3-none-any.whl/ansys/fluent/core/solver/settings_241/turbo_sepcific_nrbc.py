#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .enable_9 import enable as enable_cls
from .discretization import discretization as discretization_cls
from .under_relaxation_1 import under_relaxation as under_relaxation_cls
from .verbosity_5 import verbosity as verbosity_cls
from .initialize import initialize as initialize_cls
from .show_status import show_status as show_status_cls
class turbo_sepcific_nrbc(Group):
    """
    'turbo_sepcific_nrbc' child.
    """

    fluent_name = "turbo-sepcific-nrbc"

    child_names = \
        ['enable', 'discretization', 'under_relaxation', 'verbosity']

    enable: enable_cls = enable_cls
    """
    enable child of turbo_sepcific_nrbc.
    """
    discretization: discretization_cls = discretization_cls
    """
    discretization child of turbo_sepcific_nrbc.
    """
    under_relaxation: under_relaxation_cls = under_relaxation_cls
    """
    under_relaxation child of turbo_sepcific_nrbc.
    """
    verbosity: verbosity_cls = verbosity_cls
    """
    verbosity child of turbo_sepcific_nrbc.
    """
    command_names = \
        ['initialize', 'show_status']

    initialize: initialize_cls = initialize_cls
    """
    initialize command of turbo_sepcific_nrbc.
    """
    show_status: show_status_cls = show_status_cls
    """
    show_status command of turbo_sepcific_nrbc.
    """
