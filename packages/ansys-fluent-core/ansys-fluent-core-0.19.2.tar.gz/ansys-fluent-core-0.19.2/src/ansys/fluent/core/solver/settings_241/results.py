#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .custom_vectors import custom_vectors as custom_vectors_cls
from .surfaces_5 import surfaces as surfaces_cls
from .graphics import graphics as graphics_cls
from .plot_6 import plot as plot_cls
from .scene import scene as scene_cls
from .animations import animations as animations_cls
from .report_1 import report as report_cls
class results(Group):
    """
    'results' child.
    """

    fluent_name = "results"

    child_names = \
        ['custom_vectors', 'surfaces', 'graphics', 'plot', 'scene',
         'animations', 'report']

    custom_vectors: custom_vectors_cls = custom_vectors_cls
    """
    custom_vectors child of results.
    """
    surfaces: surfaces_cls = surfaces_cls
    """
    surfaces child of results.
    """
    graphics: graphics_cls = graphics_cls
    """
    graphics child of results.
    """
    plot: plot_cls = plot_cls
    """
    plot child of results.
    """
    scene: scene_cls = scene_cls
    """
    scene child of results.
    """
    animations: animations_cls = animations_cls
    """
    animations child of results.
    """
    report: report_cls = report_cls
    """
    report child of results.
    """
