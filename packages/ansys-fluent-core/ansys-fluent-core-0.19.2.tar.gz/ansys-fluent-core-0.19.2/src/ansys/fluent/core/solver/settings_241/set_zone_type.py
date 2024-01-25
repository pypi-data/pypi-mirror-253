#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .zone_list import zone_list as zone_list_cls
from .new_type import new_type as new_type_cls
class set_zone_type(Command):
    """
    'set_zone_type' command.
    
    Parameters
    ----------
        zone_list : typing.List[str]
            Enter zone name list.
        new_type : str
            'new_type' child.
    
    """

    fluent_name = "set-zone-type"

    argument_names = \
        ['zone_list', 'new_type']

    zone_list: zone_list_cls = zone_list_cls
    """
    zone_list argument of set_zone_type.
    """
    new_type: new_type_cls = new_type_cls
    """
    new_type argument of set_zone_type.
    """
