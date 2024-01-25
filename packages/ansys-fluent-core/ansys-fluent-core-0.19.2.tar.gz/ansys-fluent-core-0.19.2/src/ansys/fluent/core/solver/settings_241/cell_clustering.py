#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .enabled_12 import enabled as enabled_cls
from .clustering_type import clustering_type as clustering_type_cls
from .nx import nx as nx_cls
from .ny import ny as ny_cls
from .nz import nz as nz_cls
from .cluster_number import cluster_number as cluster_number_cls
from .target_variable import target_variable as target_variable_cls
from .udf_name import udf_name as udf_name_cls
class cell_clustering(Group):
    """
    'cell_clustering' child.
    """

    fluent_name = "cell-clustering"

    child_names = \
        ['enabled', 'clustering_type', 'nx', 'ny', 'nz', 'cluster_number',
         'target_variable', 'udf_name']

    enabled: enabled_cls = enabled_cls
    """
    enabled child of cell_clustering.
    """
    clustering_type: clustering_type_cls = clustering_type_cls
    """
    clustering_type child of cell_clustering.
    """
    nx: nx_cls = nx_cls
    """
    nx child of cell_clustering.
    """
    ny: ny_cls = ny_cls
    """
    ny child of cell_clustering.
    """
    nz: nz_cls = nz_cls
    """
    nz child of cell_clustering.
    """
    cluster_number: cluster_number_cls = cluster_number_cls
    """
    cluster_number child of cell_clustering.
    """
    target_variable: target_variable_cls = target_variable_cls
    """
    target_variable child of cell_clustering.
    """
    udf_name: udf_name_cls = udf_name_cls
    """
    udf_name child of cell_clustering.
    """
