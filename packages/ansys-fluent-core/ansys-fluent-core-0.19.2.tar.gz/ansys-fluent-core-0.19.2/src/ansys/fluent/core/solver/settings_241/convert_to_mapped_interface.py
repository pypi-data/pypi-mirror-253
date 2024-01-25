#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .all import all as all_cls
from .auto import auto as auto_cls
from .use_local_edge_length_factor import use_local_edge_length_factor as use_local_edge_length_factor_cls
from .gtol_length_factor import gtol_length_factor as gtol_length_factor_cls
from .gtol_absolute_value import gtol_absolute_value as gtol_absolute_value_cls
class convert_to_mapped_interface(Command):
    """
    Convert non-conformal mesh interface to mapped mesh interfaces.
    
    Parameters
    ----------
        all : bool
            Convert all mesh interfaces to mapped mesh interfaces.
        auto : bool
            Convert poorly matching mesh interfaces to mapped mesh interfaces.
        use_local_edge_length_factor : bool
            Enable tolerance based on local edge length factor instead of absolute tolerance.
        gtol_length_factor : real
            'gtol_length_factor' child.
        gtol_absolute_value : real
            'gtol_absolute_value' child.
    
    """

    fluent_name = "convert-to-mapped-interface"

    argument_names = \
        ['all', 'auto', 'use_local_edge_length_factor', 'gtol_length_factor',
         'gtol_absolute_value']

    all: all_cls = all_cls
    """
    all argument of convert_to_mapped_interface.
    """
    auto: auto_cls = auto_cls
    """
    auto argument of convert_to_mapped_interface.
    """
    use_local_edge_length_factor: use_local_edge_length_factor_cls = use_local_edge_length_factor_cls
    """
    use_local_edge_length_factor argument of convert_to_mapped_interface.
    """
    gtol_length_factor: gtol_length_factor_cls = gtol_length_factor_cls
    """
    gtol_length_factor argument of convert_to_mapped_interface.
    """
    gtol_absolute_value: gtol_absolute_value_cls = gtol_absolute_value_cls
    """
    gtol_absolute_value argument of convert_to_mapped_interface.
    """
