#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .cell_deactivate_list import cell_deactivate_list as cell_deactivate_list_cls
class deactivate_cell_zone(Command):
    """
    Deactivate cell thread.
    
    Parameters
    ----------
        cell_deactivate_list : typing.List[str]
            Deactivate a cell zone.
    
    """

    fluent_name = "deactivate-cell-zone"

    argument_names = \
        ['cell_deactivate_list']

    cell_deactivate_list: cell_deactivate_list_cls = cell_deactivate_list_cls
    """
    cell_deactivate_list argument of deactivate_cell_zone.
    """
