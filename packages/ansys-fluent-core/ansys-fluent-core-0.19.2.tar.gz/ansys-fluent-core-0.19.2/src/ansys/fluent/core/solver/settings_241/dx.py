#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .file_name_1 import file_name as file_name_cls
from .surfaces import surfaces as surfaces_cls
from .techplot_scalars import techplot_scalars as techplot_scalars_cls
class dx(Command):
    """
    Write an IBM Data Explorer format file.
    
    Parameters
    ----------
        file_name : str
            'file_name' child.
        surfaces : typing.List[str]
            Select surface.
        techplot_scalars : typing.List[str]
            'techplot_scalars' child.
    
    """

    fluent_name = "dx"

    argument_names = \
        ['file_name', 'surfaces', 'techplot_scalars']

    file_name: file_name_cls = file_name_cls
    """
    file_name argument of dx.
    """
    surfaces: surfaces_cls = surfaces_cls
    """
    surfaces argument of dx.
    """
    techplot_scalars: techplot_scalars_cls = techplot_scalars_cls
    """
    techplot_scalars argument of dx.
    """
