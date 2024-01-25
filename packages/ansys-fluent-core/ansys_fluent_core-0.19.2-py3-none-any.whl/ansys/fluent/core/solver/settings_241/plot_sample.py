#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .sample import sample as sample_cls
from .variable_to_sample import variable_to_sample as variable_to_sample_cls
from .weighting_variable import weighting_variable as weighting_variable_cls
from .correlation_variable import correlation_variable as correlation_variable_cls
from .file_name_1 import file_name as file_name_cls
class plot_sample(Command):
    """
    'plot_sample' command.
    
    Parameters
    ----------
        sample : str
            'sample' child.
        variable_to_sample : str
            'variable_to_sample' child.
        weighting_variable : str
            'weighting_variable' child.
        correlation_variable : str
            'correlation_variable' child.
        file_name : str
            'file_name' child.
    
    """

    fluent_name = "plot-sample"

    argument_names = \
        ['sample', 'variable_to_sample', 'weighting_variable',
         'correlation_variable', 'file_name']

    sample: sample_cls = sample_cls
    """
    sample argument of plot_sample.
    """
    variable_to_sample: variable_to_sample_cls = variable_to_sample_cls
    """
    variable_to_sample argument of plot_sample.
    """
    weighting_variable: weighting_variable_cls = weighting_variable_cls
    """
    weighting_variable argument of plot_sample.
    """
    correlation_variable: correlation_variable_cls = correlation_variable_cls
    """
    correlation_variable argument of plot_sample.
    """
    file_name: file_name_cls = file_name_cls
    """
    file_name argument of plot_sample.
    """
