#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .setup_method import setup_method as setup_method_cls
from .model_setup import model_setup as model_setup_cls
from .read_input_file import read_input_file as read_input_file_cls
class perforated_wall(Group):
    """
    Perforated wall model.
    """

    fluent_name = "perforated-wall"

    child_names = \
        ['setup_method', 'model_setup']

    setup_method: setup_method_cls = setup_method_cls
    """
    setup_method child of perforated_wall.
    """
    model_setup: model_setup_cls = model_setup_cls
    """
    model_setup child of perforated_wall.
    """
    command_names = \
        ['read_input_file']

    read_input_file: read_input_file_cls = read_input_file_cls
    """
    read_input_file command of perforated_wall.
    """
