#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .sigma import sigma as sigma_cls
from .sigma2 import sigma2 as sigma2_cls
from .relax import relax as relax_cls
from .tangential_source import tangential_source as tangential_source_cls
from .verbosity_4 import verbosity as verbosity_cls
class general_nrbc(Group):
    """
    'general_nrbc' child.
    """

    fluent_name = "general-nrbc"

    child_names = \
        ['sigma', 'sigma2', 'relax', 'tangential_source', 'verbosity']

    sigma: sigma_cls = sigma_cls
    """
    sigma child of general_nrbc.
    """
    sigma2: sigma2_cls = sigma2_cls
    """
    sigma2 child of general_nrbc.
    """
    relax: relax_cls = relax_cls
    """
    relax child of general_nrbc.
    """
    tangential_source: tangential_source_cls = tangential_source_cls
    """
    tangential_source child of general_nrbc.
    """
    verbosity: verbosity_cls = verbosity_cls
    """
    verbosity child of general_nrbc.
    """
