# vectors/__init__.py
# This makes the vectors directory a Python package and exposes the data

from .word_vectors import get_word_vectors
from .clusters import get_clusters
from .clusters import get_cluster_names
from .colors import get_colors

# Call the functions to get the actual data
word_vectors = get_word_vectors()
clusters = get_clusters()
colors = get_colors()
clusters_names = get_cluster_names()

__all__ = ['word_vectors', 'clusters', 'colors', 'clusters_names']
