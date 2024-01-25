#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .enabled_14 import enabled as enabled_cls
from .source_file import source_file as source_file_cls
from .create_customized_addon_lib import create_customized_addon_lib as create_customized_addon_lib_cls
class customized_udf(Group):
    """
    'customized_udf' child.
    """

    fluent_name = "customized-udf"

    child_names = \
        ['enabled', 'source_file']

    enabled: enabled_cls = enabled_cls
    """
    enabled child of customized_udf.
    """
    source_file: source_file_cls = source_file_cls
    """
    source_file child of customized_udf.
    """
    command_names = \
        ['create_customized_addon_lib']

    create_customized_addon_lib: create_customized_addon_lib_cls = create_customized_addon_lib_cls
    """
    create_customized_addon_lib command of customized_udf.
    """
