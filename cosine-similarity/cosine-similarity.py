import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    if np.linalg.norm(a) == 0 or np.linalg.norm(b) == 0:
        cosin = 0
    else:
        cosin = np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))
    
    return float(cosin)