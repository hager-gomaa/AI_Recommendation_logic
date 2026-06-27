# 🎬 AI Recommendation Logic

A simple content-based recommendation system that suggests movies based on a user's genre preferences, using Jaccard similarity to match interests against a small movie catalog.

## 📌 Overview

| | |
|---|---|
| **Goal** | Recommend items based on user preferences |
| **Technique** | Content-based filtering with Jaccard similarity |
| **Language** | Python 3 |
| **Dependencies** | None — built with the Python standard library |

## ✨ Features

- Takes user input as a comma-separated list of favorite genres
- Computes similarity between user preferences and each movie's genre set using **Jaccard similarity** (intersection over union)
- Ranks and displays the top matching recommendations with their match percentage
- Easily extendable catalog (`movies` list of dictionaries)

## 🛠️ Key Skills Demonstrated

- Logic building and pattern matching
- Set operations in Python
- Recommendation system fundamentals (similarity scoring, ranking)
- Clean separation of data, scoring logic, and I/O

## 🚀 Getting Started

### Prerequisites
- Python 3.7+

### Run it
```bash
python project3_recommender.py
```

### Example session
```
Available genres: action, adventure, comedy, drama, family, horror, romance, sci-fi, thriller
Enter your favorite genres (comma separated): action, sci-fi

🎬 Recommended movies for you:
 - The Matrix  (match: 100% | genres: action, sci-fi)
 - Inception  (match: 67% | genres: thriller, action, sci-fi)
 - John Wick  (match: 33% | genres: thriller, action)
```

## 📂 Project Structure
```
.
└── project3_recommender.py
```

## 🔮 Possible Extensions
- Load a larger movie catalog from a CSV or public API (e.g. TMDB)
- Use TF-IDF or embeddings (e.g. SentenceTransformers) for richer similarity matching
- Add collaborative filtering based on multiple users' ratings
- Wrap it in a Streamlit app for an interactive UI

## 📄 License
This project is open source and available under the [MIT License](LICENSE).
