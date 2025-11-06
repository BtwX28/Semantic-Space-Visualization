# plot_semantic_space.py
# Main script to visualize the semantic space using modularized data
# Uses both matplotlib (headless-friendly) and Plotly (for interactive HTML)

import matplotlib.pyplot as plt
import numpy as np

def create_semantic_space_plot(colors, clusters, word_vectors):
    # Create a simple plot to represent the semantic space
    fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(3.5, 2.5), layout="constrained") # Number of rows and columns
    
    # Get the first two cluster names for axis labels
    cluster_names = list(clusters.keys())
    x_axis_label = cluster_names[0] if len(cluster_names) > 0 else "Dimension 1"
    y_axis_label = cluster_names[1] if len(cluster_names) > 1 else "Dimension 2"

    for cluster_name, words in clusters.items():
        for word in words:
            ax.scatter(word_vectors[word][0], word_vectors[word][1], color=colors[cluster_name])
            ax.text(word_vectors[word][0], word_vectors[word][1], word)

    # Set axis labels based on first two cluster names
    ax.set_xlabel(f'{x_axis_label}')
    ax.set_ylabel(f'{y_axis_label}')
    
    fig.suptitle('Semantic Space Visualization', fontsize=15)
    fig = plt.gcf()
    fig.set_size_inches(10, 8)
    plt.savefig('semantic_space_visualization.png', dpi=300)
    return fig, ax
