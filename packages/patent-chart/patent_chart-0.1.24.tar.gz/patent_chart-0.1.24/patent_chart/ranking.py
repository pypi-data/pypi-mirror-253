import numpy as np
from sentence_transformers import SentenceTransformer

from .data_structures import GeneratedPassage

ranking_model_version = 'all-MiniLM-L6-v2'

model = SentenceTransformer('all-MiniLM-L6-v2')

def cosine_similarity(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def find_most_similar_chunks(embeddings: np.ndarray, ref: np.ndarray):
    similarities: list[np.ndarray] = []
    for embedding in embeddings:
        similarities.append(cosine_similarity(ref, embedding))

    similarities = np.vstack(similarities).reshape(-1)
    return np.argsort(similarities)[::-1]

def rank_passages(passages: list[GeneratedPassage], claim_element: str):
    """
    Mutates the ranking attribute of each passage in the list
    """
    claim_element_embedding = model.encode(claim_element)
    passage_embeddings = model.encode([passage.text for passage in passages])
    sorted_indices = find_most_similar_chunks(passage_embeddings, claim_element_embedding)
    
    for i, sorted_idx in enumerate(sorted_indices):
        passages[sorted_idx].ranking = i + 1
        passages[sorted_idx].ranking_model_version = ranking_model_version

    return passages