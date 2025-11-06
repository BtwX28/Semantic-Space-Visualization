# word_vectors.py
# Contains the word_vectors dictionary for the semantic space visualization

def get_word_vectors():
    word_vectors = {
        # Elektronik cluster
        "Strom": [0.200, 0.300, 0.250],
        "Technik": [0.240, 0.350, 0.300],
        "Elektronische_Musik": [0.160, 0.370, 0.220],
        # Technology cluster
        "Internet": [0.800, 0.800, 0.800],
        "Router": [0.830, 0.820, 0.770],
        "IP": [0.770, 0.850, 0.830],
        # Music cluster
        "Jazz": [0.400, 0.900, 0.950],
        "Musik": [0.440, 0.880, 0.920],
        #"test_word": [x, y]
    }
    return word_vectors
