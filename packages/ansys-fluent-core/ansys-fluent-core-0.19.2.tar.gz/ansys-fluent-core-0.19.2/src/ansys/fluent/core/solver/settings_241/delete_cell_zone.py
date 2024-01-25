#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .cell_zones_2 import cell_zones as cell_zones_cls
class delete_cell_zone(Command):
    """
    Delete a cell thread.
    
    Parameters
    ----------
        cell_zones : typing.List[str]
            Delete a cell zone.
    
    """

    fluent_name = "delete-cell-zone"

    argument_names = \
        ['cell_zones']

    cell_zones: cell_zones_cls = cell_zones_cls
    """
    cell_zones argument of delete_cell_zone.
    """
