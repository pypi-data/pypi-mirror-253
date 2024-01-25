#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .driver_name import driver_name as driver_name_cls
class driver(Command):
    """
    Change the current graphics driver.
    
    Parameters
    ----------
        driver_name : str
            'driver_name' child.
    
    """

    fluent_name = "driver"

    argument_names = \
        ['driver_name']

    driver_name: driver_name_cls = driver_name_cls
    """
    driver_name argument of driver.
    """
