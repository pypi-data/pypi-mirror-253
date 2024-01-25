#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .zone_name_1 import zone_name as zone_name_cls
from .new_name import new_name as new_name_cls
class zone_name(Command):
    """
    Give a zone a new name.
    
    Parameters
    ----------
        zone_name : str
            Enter a zone name.
        new_name : str
            'new_name' child.
    
    """

    fluent_name = "zone-name"

    argument_names = \
        ['zone_name', 'new_name']

    zone_name: zone_name_cls = zone_name_cls
    """
    zone_name argument of zone_name.
    """
    new_name: new_name_cls = new_name_cls
    """
    new_name argument of zone_name.
    """
