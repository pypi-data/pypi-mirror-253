#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .lti_folder_name import lti_folder_name as lti_folder_name_cls
from .user_config import user_config as user_config_cls
from .min_order import min_order as min_order_cls
from .max_order import max_order as max_order_cls
from .rel_error import rel_error as rel_error_cls
from .tolerance_0th_order import tolerance_0th_order as tolerance_0th_order_cls
from .slope_method import slope_method as slope_method_cls
from .run_rom_generation import run_rom_generation as run_rom_generation_cls
class lti_rom_generation(Group):
    """
    'lti_rom_generation' child.
    """

    fluent_name = "lti-rom-generation"

    child_names = \
        ['lti_folder_name', 'user_config', 'min_order', 'max_order',
         'rel_error', 'tolerance_0th_order', 'slope_method']

    lti_folder_name: lti_folder_name_cls = lti_folder_name_cls
    """
    lti_folder_name child of lti_rom_generation.
    """
    user_config: user_config_cls = user_config_cls
    """
    user_config child of lti_rom_generation.
    """
    min_order: min_order_cls = min_order_cls
    """
    min_order child of lti_rom_generation.
    """
    max_order: max_order_cls = max_order_cls
    """
    max_order child of lti_rom_generation.
    """
    rel_error: rel_error_cls = rel_error_cls
    """
    rel_error child of lti_rom_generation.
    """
    tolerance_0th_order: tolerance_0th_order_cls = tolerance_0th_order_cls
    """
    tolerance_0th_order child of lti_rom_generation.
    """
    slope_method: slope_method_cls = slope_method_cls
    """
    slope_method child of lti_rom_generation.
    """
    command_names = \
        ['run_rom_generation']

    run_rom_generation: run_rom_generation_cls = run_rom_generation_cls
    """
    run_rom_generation command of lti_rom_generation.
    """
