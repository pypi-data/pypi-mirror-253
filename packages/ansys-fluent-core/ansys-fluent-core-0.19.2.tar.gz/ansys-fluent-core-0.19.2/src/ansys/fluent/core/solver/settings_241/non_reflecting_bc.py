#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .general_nrbc import general_nrbc as general_nrbc_cls
from .turbo_sepcific_nrbc import turbo_sepcific_nrbc as turbo_sepcific_nrbc_cls
class non_reflecting_bc(Group):
    """
    'non_reflecting_bc' child.
    """

    fluent_name = "non-reflecting-bc"

    child_names = \
        ['general_nrbc', 'turbo_sepcific_nrbc']

    general_nrbc: general_nrbc_cls = general_nrbc_cls
    """
    general_nrbc child of non_reflecting_bc.
    """
    turbo_sepcific_nrbc: turbo_sepcific_nrbc_cls = turbo_sepcific_nrbc_cls
    """
    turbo_sepcific_nrbc child of non_reflecting_bc.
    """
