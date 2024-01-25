#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .length import length as length_cls
from .boundary import boundary as boundary_cls
class knudsen_number_calculator(Command):
    """
    Utility to compute Kudsen number based on characteristic length and boundary information.
    
    Parameters
    ----------
        length : real
            Characteristic physics length.
        boundary : str
            'boundary' child.
    
    """

    fluent_name = "knudsen-number-calculator"

    argument_names = \
        ['length', 'boundary']

    length: length_cls = length_cls
    """
    length argument of knudsen_number_calculator.
    """
    boundary: boundary_cls = boundary_cls
    """
    boundary argument of knudsen_number_calculator.
    """
