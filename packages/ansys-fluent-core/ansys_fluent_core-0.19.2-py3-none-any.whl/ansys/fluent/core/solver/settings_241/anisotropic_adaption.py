#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .operations import operations as operations_cls
from .iterations import iterations as iterations_cls
from .fixed_zones import fixed_zones as fixed_zones_cls
from .indicator import indicator as indicator_cls
from .target import target as target_cls
from .maximum_anisotropic_ratio import maximum_anisotropic_ratio as maximum_anisotropic_ratio_cls
from .minimum_edge_length_1 import minimum_edge_length as minimum_edge_length_cls
from .minimum_cell_quality_1 import minimum_cell_quality as minimum_cell_quality_cls
from .adapt_mesh_1 import adapt_mesh as adapt_mesh_cls
class anisotropic_adaption(Group):
    """
    Enter the anisotropic adaption menu.
    """

    fluent_name = "anisotropic-adaption"

    child_names = \
        ['operations', 'iterations', 'fixed_zones', 'indicator', 'target',
         'maximum_anisotropic_ratio', 'minimum_edge_length',
         'minimum_cell_quality']

    operations: operations_cls = operations_cls
    """
    operations child of anisotropic_adaption.
    """
    iterations: iterations_cls = iterations_cls
    """
    iterations child of anisotropic_adaption.
    """
    fixed_zones: fixed_zones_cls = fixed_zones_cls
    """
    fixed_zones child of anisotropic_adaption.
    """
    indicator: indicator_cls = indicator_cls
    """
    indicator child of anisotropic_adaption.
    """
    target: target_cls = target_cls
    """
    target child of anisotropic_adaption.
    """
    maximum_anisotropic_ratio: maximum_anisotropic_ratio_cls = maximum_anisotropic_ratio_cls
    """
    maximum_anisotropic_ratio child of anisotropic_adaption.
    """
    minimum_edge_length: minimum_edge_length_cls = minimum_edge_length_cls
    """
    minimum_edge_length child of anisotropic_adaption.
    """
    minimum_cell_quality: minimum_cell_quality_cls = minimum_cell_quality_cls
    """
    minimum_cell_quality child of anisotropic_adaption.
    """
    command_names = \
        ['adapt_mesh']

    adapt_mesh: adapt_mesh_cls = adapt_mesh_cls
    """
    adapt_mesh command of anisotropic_adaption.
    """
