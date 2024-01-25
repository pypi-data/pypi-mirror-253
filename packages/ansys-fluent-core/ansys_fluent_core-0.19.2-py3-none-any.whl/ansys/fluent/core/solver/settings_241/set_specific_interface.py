#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .interface_number import interface_number as interface_number_cls
from .bands import bands as bands_cls
class set_specific_interface(Command):
    """
    Set number of band to be used for mixing.
    
    Parameters
    ----------
        interface_number : int
            Set number of band to be used for mixing.
        bands : int
            Set number of band to be used for mixing.
    
    """

    fluent_name = "set-specific-interface"

    argument_names = \
        ['interface_number', 'bands']

    interface_number: interface_number_cls = interface_number_cls
    """
    interface_number argument of set_specific_interface.
    """
    bands: bands_cls = bands_cls
    """
    bands argument of set_specific_interface.
    """
