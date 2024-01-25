#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .enable_scale_all import enable_scale_all as enable_scale_all_cls
from .disable_scale_all import disable_scale_all as disable_scale_all_cls
from .interface_name_1 import interface_name as interface_name_cls
from .scale_2 import scale as scale_cls
class enforce_flux_scaling(Command):
    """
    Enforce flux scaling ON/OFF at the turbo interfaces.
    
    Parameters
    ----------
        enable_scale_all : bool
            Scale scaling of all the interfaces...
        disable_scale_all : bool
            Disable scaling of all the interfaces...
        interface_name : str
            'interface_name' child.
        scale : bool
            Enable flux scaling at mixing plane interface.
    
    """

    fluent_name = "enforce-flux-scaling"

    argument_names = \
        ['enable_scale_all', 'disable_scale_all', 'interface_name', 'scale']

    enable_scale_all: enable_scale_all_cls = enable_scale_all_cls
    """
    enable_scale_all argument of enforce_flux_scaling.
    """
    disable_scale_all: disable_scale_all_cls = disable_scale_all_cls
    """
    disable_scale_all argument of enforce_flux_scaling.
    """
    interface_name: interface_name_cls = interface_name_cls
    """
    interface_name argument of enforce_flux_scaling.
    """
    scale: scale_cls = scale_cls
    """
    scale argument of enforce_flux_scaling.
    """
