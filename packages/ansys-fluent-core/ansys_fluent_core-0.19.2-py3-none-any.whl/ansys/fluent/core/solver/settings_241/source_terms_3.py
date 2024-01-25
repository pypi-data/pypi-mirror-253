#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .sources import sources as sources_cls
from .source_terms_2 import source_terms as source_terms_cls
class source_terms(Group):
    """
    Help not available.
    """

    fluent_name = "source-terms"

    child_names = \
        ['sources', 'source_terms']

    sources: sources_cls = sources_cls
    """
    sources child of source_terms.
    """
    source_terms: source_terms_cls = source_terms_cls
    """
    source_terms child of source_terms.
    """
