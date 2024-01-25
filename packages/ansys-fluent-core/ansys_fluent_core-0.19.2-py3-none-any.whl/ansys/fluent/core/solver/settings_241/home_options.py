#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .field_name_1 import field_name as field_name_cls
from .data_source import data_source as data_source_cls
from .range_options import range_options as range_options_cls
from .rendering_quality import rendering_quality as rendering_quality_cls
from .color_density import color_density as color_density_cls
from .colormap_options import colormap_options as colormap_options_cls
from .cell_zones_3 import cell_zones as cell_zones_cls
class home_options(Group):
    """
    'home_options' child.
    """

    fluent_name = "home-options"

    child_names = \
        ['field_name', 'data_source', 'range_options', 'rendering_quality',
         'color_density', 'colormap_options', 'cell_zones']

    field_name: field_name_cls = field_name_cls
    """
    field_name child of home_options.
    """
    data_source: data_source_cls = data_source_cls
    """
    data_source child of home_options.
    """
    range_options: range_options_cls = range_options_cls
    """
    range_options child of home_options.
    """
    rendering_quality: rendering_quality_cls = rendering_quality_cls
    """
    rendering_quality child of home_options.
    """
    color_density: color_density_cls = color_density_cls
    """
    color_density child of home_options.
    """
    colormap_options: colormap_options_cls = colormap_options_cls
    """
    colormap_options child of home_options.
    """
    cell_zones: cell_zones_cls = cell_zones_cls
    """
    cell_zones child of home_options.
    """
