movies = [
    {"title": "Inception",      "genres": {"sci-fi", "thriller", "action"}},
    {"title": "The Notebook",   "genres": {"romance", "drama"}},
    {"title": "Interstellar",   "genres": {"sci-fi", "drama", "adventure"}},
    {"title": "The Hangover",   "genres": {"comedy"}},
    {"title": "John Wick",      "genres": {"action", "thriller"}},
    {"title": "Titanic",        "genres": {"romance", "drama"}},
    {"title": "The Conjuring",  "genres": {"horror", "thriller"}},
    {"title": "Toy Story",      "genres": {"comedy", "adventure", "family"}},
    {"title": "The Matrix",     "genres": {"sci-fi", "action"}},
    {"title": "Coco",           "genres": {"family", "adventure", "drama"}},
]


def jaccard_similarity(set1: set, set2: set) -> float:
    """Returns similarity score between 0 and 1."""
    if not set1 or not set2:
        return 0.0
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union


def recommend(user_genres: set, catalog: list, top_n: int = 3) -> list:
    scored = []
    for movie in catalog:
        score = jaccard_similarity(user_genres, movie["genres"])
        if score > 0:
            scored.append((movie["title"], score, movie["genres"]))

    scored.sort(key=lambda item: item[1], reverse=True)
    return scored[:top_n]


def get_user_preferences() -> set:
    all_genres = sorted({g for m in movies for g in m["genres"]})
    print("Available genres:", ", ".join(all_genres))
    user_input = input("Enter your favorite genres (comma separated): ")
    return {g.strip().lower() for g in user_input.split(",") if g.strip()}


def main():
    user_genres = get_user_preferences()
    results = recommend(user_genres, movies)

    if not results:
        print("\nNo matching recommendations found. Try different genres!")
        return

    print("\n🎬 Recommended movies for you:")
    for title, score, genres in results:
        print(f" - {title}  (match: {score:.0%} | genres: {', '.join(genres)})")


if __name__ == "__main__":
    main()