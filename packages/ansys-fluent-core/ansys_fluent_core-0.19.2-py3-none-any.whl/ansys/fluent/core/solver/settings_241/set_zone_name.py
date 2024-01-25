#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .zonename import zonename as zonename_cls
from .newname import newname as newname_cls
class set_zone_name(Command):
    """
    Give a zone a new name.
    
    Parameters
    ----------
        zonename : str
            Enter a zone name.
        newname : str
            'newname' child.
    
    """

    fluent_name = "set-zone-name"

    argument_names = \
        ['zonename', 'newname']

    zonename: zonename_cls = zonename_cls
    """
    zonename argument of set_zone_name.
    """
    newname: newname_cls = newname_cls
    """
    newname argument of set_zone_name.
    """
