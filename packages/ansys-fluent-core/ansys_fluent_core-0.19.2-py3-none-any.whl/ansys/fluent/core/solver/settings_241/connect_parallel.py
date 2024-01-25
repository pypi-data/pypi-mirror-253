#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .schost import schost as schost_cls
from .scport import scport as scport_cls
from .scname import scname as scname_cls
class connect_parallel(Command):
    """
    System coupling connection status.
    
    Parameters
    ----------
        schost : str
            Sc solver host input.
        scport : int
            Sc solver port input.
        scname : str
            Sc solver name input.
    
    """

    fluent_name = "connect-parallel"

    argument_names = \
        ['schost', 'scport', 'scname']

    schost: schost_cls = schost_cls
    """
    schost argument of connect_parallel.
    """
    scport: scport_cls = scport_cls
    """
    scport argument of connect_parallel.
    """
    scname: scname_cls = scname_cls
    """
    scname argument of connect_parallel.
    """
