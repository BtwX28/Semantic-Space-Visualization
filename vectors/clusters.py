# clusters.py
# Contains the clusters dictionary for the semantic space visualization

def get_clusters():
    clusters = {
        "Elektronik": ["Strom", "Technik", "Elektronische_Musik"],
        "Technik": ["Internet", "Router", "IP"],
        "Musik": ["Jazz", "Musik"]
    }
    return clusters

def get_cluster_names():
    """Returns only the cluster names as a list"""
    return list(get_clusters().keys())
