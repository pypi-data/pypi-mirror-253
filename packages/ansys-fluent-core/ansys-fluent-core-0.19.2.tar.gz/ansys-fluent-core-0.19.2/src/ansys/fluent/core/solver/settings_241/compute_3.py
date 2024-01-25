#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .injections_1 import injections as injections_cls
from .boundaries_1 import boundaries as boundaries_cls
from .lines_1 import lines as lines_cls
from .planes import planes as planes_cls
from .op_udf import op_udf as op_udf_cls
from .append_sample import append_sample as append_sample_cls
from .accumulate_rates import accumulate_rates as accumulate_rates_cls
class compute(Command):
    """
    'compute' command.
    
    Parameters
    ----------
        injections : typing.List[str]
            'injections' child.
        boundaries : typing.List[str]
            'boundaries' child.
        lines : typing.List[str]
            Select surface.
        planes : typing.List[str]
            Select surface.
        op_udf : str
            'op_udf' child.
        append_sample : bool
            'append_sample' child.
        accumulate_rates : bool
            'accumulate_rates' child.
    
    """

    fluent_name = "compute"

    argument_names = \
        ['injections', 'boundaries', 'lines', 'planes', 'op_udf',
         'append_sample', 'accumulate_rates']

    injections: injections_cls = injections_cls
    """
    injections argument of compute.
    """
    boundaries: boundaries_cls = boundaries_cls
    """
    boundaries argument of compute.
    """
    lines: lines_cls = lines_cls
    """
    lines argument of compute.
    """
    planes: planes_cls = planes_cls
    """
    planes argument of compute.
    """
    op_udf: op_udf_cls = op_udf_cls
    """
    op_udf argument of compute.
    """
    append_sample: append_sample_cls = append_sample_cls
    """
    append_sample argument of compute.
    """
    accumulate_rates: accumulate_rates_cls = accumulate_rates_cls
    """
    accumulate_rates argument of compute.
    """
