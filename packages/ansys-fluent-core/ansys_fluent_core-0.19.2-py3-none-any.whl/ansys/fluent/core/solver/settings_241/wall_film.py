#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .convective_heat_transfer import convective_heat_transfer as convective_heat_transfer_cls
from .include_convective_heat_transfer import include_convective_heat_transfer as include_convective_heat_transfer_cls
from .film_movement import film_movement as film_movement_cls
from .film_adds_to_dpm_concentration import film_adds_to_dpm_concentration as film_adds_to_dpm_concentration_cls
from .temperature_limiter import temperature_limiter as temperature_limiter_cls
class wall_film(Group):
    """
    'wall_film' child.
    """

    fluent_name = "wall-film"

    child_names = \
        ['convective_heat_transfer', 'include_convective_heat_transfer',
         'film_movement', 'film_adds_to_dpm_concentration',
         'temperature_limiter']

    convective_heat_transfer: convective_heat_transfer_cls = convective_heat_transfer_cls
    """
    convective_heat_transfer child of wall_film.
    """
    include_convective_heat_transfer: include_convective_heat_transfer_cls = include_convective_heat_transfer_cls
    """
    include_convective_heat_transfer child of wall_film.
    """
    film_movement: film_movement_cls = film_movement_cls
    """
    film_movement child of wall_film.
    """
    film_adds_to_dpm_concentration: film_adds_to_dpm_concentration_cls = film_adds_to_dpm_concentration_cls
    """
    film_adds_to_dpm_concentration child of wall_film.
    """
    temperature_limiter: temperature_limiter_cls = temperature_limiter_cls
    """
    temperature_limiter child of wall_film.
    """
