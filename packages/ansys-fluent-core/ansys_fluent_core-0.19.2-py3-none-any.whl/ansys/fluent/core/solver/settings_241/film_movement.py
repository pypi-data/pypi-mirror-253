#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .condensing_film_stationary import condensing_film_stationary as condensing_film_stationary_cls
from .all_film_stationary import all_film_stationary as all_film_stationary_cls
class film_movement(Group):
    """
    Set options for controlling the film particles movement.
    """

    fluent_name = "film-movement"

    child_names = \
        ['condensing_film_stationary', 'all_film_stationary']

    condensing_film_stationary: condensing_film_stationary_cls = condensing_film_stationary_cls
    """
    condensing_film_stationary child of film_movement.
    """
    all_film_stationary: all_film_stationary_cls = all_film_stationary_cls
    """
    all_film_stationary child of film_movement.
    """
