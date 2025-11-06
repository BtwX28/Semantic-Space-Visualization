#!/usr/bin/env python3
"""
Main entry point for the 3D Semantic Space Visualization
This script combines all modules and generates both static and interactive plots.
"""

import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import vectors
import plot_semantic_space as pss

pss.create_semantic_space_plot(vectors.colors, vectors.clusters, vectors.word_vectors)

