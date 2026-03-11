def score_hybrid(
    similarity_embedding: float,
    match_tags: float,
    quality: float,
    popularity: float,
    novelty: float,
) -> float:
    return (
        0.45 * similarity_embedding
        + 0.25 * match_tags
        + 0.15 * quality
        + 0.10 * popularity
        + 0.05 * novelty
    )
