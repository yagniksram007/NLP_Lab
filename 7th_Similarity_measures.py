# D1: It is going to rain today"
# D2: Today Rama is not going outside to watch ruin"
# D3: "I am going to watch the movie tomorrow with Rama
# D4: "Tomorrow Rama is going to watch the ruin at sen shore"
# Find the top two relevant documents for the query document with the content "Rama
# watching the rain" using the latent semantic space model. Use the following similarity measure and show the result analysis using har chart.
# a) Euclidean distance
# b ) Cosine similarity
# c) Jaccard similarity 
# d) Dice Similarity Coefficient

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances, cosine_similarity
from sklearn.metrics import jaccard_score
from scipy.spatial.distance import dice

# Define the documents and the query
documents = [
    "It is going to rain today",
    "Today Rama is not going outside to watch ruin",
    "I am going to watch the movie tomorrow with Rama",
    "Tomorrow Rama is going to watch the ruin at sen shore"
]
query = "Rama watching the rain"

# Combine the documents and query for vectorization
all_docs = documents + [query]

# Vectorize the documents
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(all_docs).toarray()

# Separate the documents and query vectors
doc_vectors = X[:-1]
query_vector = X[-1].reshape(1, -1)

# Euclidean Distance
euclidean_dist = euclidean_distances(doc_vectors, query_vector).flatten()
euclidean_sorted_indices = np.argsort(euclidean_dist)[:2]

# Cosine Similarity
cosine_sim = cosine_similarity(doc_vectors, query_vector).flatten()
cosine_sorted_indices = np.argsort(cosine_sim)[-2:][::-1]

# Jaccard Similarity
def jaccard_similarity(query_vector, doc_vectors):
    similarities = []
    for doc_vector in doc_vectors:
        score = jaccard_score(query_vector, doc_vector, average='binary')
        similarities.append(score)
    return np.array(similarities)

jaccard_sim = jaccard_similarity(query_vector.flatten(), doc_vectors)
jaccard_sorted_indices = np.argsort(jaccard_sim)[-2:][::-1]

# Dice Similarity Coefficient
def dice_similarity(query_vector, doc_vectors):
    similarities = []
    for doc_vector in doc_vectors:
        score = 1 - dice(query_vector, doc_vector)
        similarities.append(score)
    return np.array(similarities)

dice_sim = dice_similarity(query_vector.flatten(), doc_vectors)
dice_sorted_indices = np.argsort(dice_sim)[-2:][::-1]

# Print the results
similarity_measures = {
    'Euclidean Distance': euclidean_sorted_indices,
    'Cosine Similarity': cosine_sorted_indices,
    'Jaccard Similarity': jaccard_sorted_indices,
    'Dice Similarity': dice_sorted_indices
}

for measure, indices in similarity_measures.items():
    print(f"\nTop 2 documents for {measure}:")
    for idx in indices:
        print(f"Document {idx+1}: {documents[idx]}")

# Plot the results
import matplotlib.pyplot as plt

measure_names = ['Euclidean', 'Cosine', 'Jaccard', 'Dice']
doc_indices = [euclidean_sorted_indices, cosine_sorted_indices, jaccard_sorted_indices, dice_sorted_indices]

fig, ax = plt.subplots()
bar_width = 0.2
index = np.arange(len(documents))

for i, indices in enumerate(doc_indices):
    ax.bar(index + i * bar_width, [1 if j in indices else 0 for j in range(len(documents))], bar_width, label=measure_names[i])

ax.set_xlabel('Documents')
ax.set_ylabel('Relevance')
ax.set_title('Top 2 Relevant Documents by Different Similarity Measures')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels([f'D{j+1}' for j in range(len(documents))])
ax.legend()

plt.show()

# Output:
# Top 2 documents for Euclidean Distance:
# Document 1: It is going to rain today
# Document 3: I am going to watch the movie tomorrow with Rama

# Top 2 documents for Cosine Similarity:
# Document 3: I am going to watch the movie tomorrow with Rama
# Document 4: Tomorrow Rama is going to watch the ruin at sen shore

# Top 2 documents for Jaccard Similarity:
# Document 3: I am going to watch the movie tomorrow with Rama
# Document 4: Tomorrow Rama is going to watch the ruin at sen shore

# Top 2 documents for Dice Similarity:
# Document 3: I am going to watch the movie tomorrow with Rama
# Document 4: Tomorrow Rama is going to watch the ruin at sen shore