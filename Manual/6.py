# 6. The dataset contains following 5 documents.
# D1: "Shipment of gold damaged in a fire"
# D2: "Delivery of silver arrived in a silver truck" D3: "Shipment of gold arrived in a truck"
# D4: “Purchased silver and gold arrived in a wooden truck” D5: “The arrival of gold and silver shipment is delayed.”
# Find the top two relevant documents for the query document with the content “gold silver truck " using the vector space model.
# Use the following similarity measure and analyze the result.
# a. Euclidean distance
# b. Manhattan distance
# c. Cosine similarity

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from scipy.spatial.distance import euclidean, cityblock
from sklearn.metrics.pairwise import cosine_similarity

# Document set
documents = [
    "Shipment of gold damaged in a fire",
    "Delivery of silver arrived in a silver truck",
    "Shipment of gold arrived in a truck",
    "Purchased silver and gold arrived in a wooden truck",
    "The arrival of gold and silver shipment is delayed."
]

# Query sentence
query = "gold silver truck"

# Initialize the CountVectorizer with stop words removed
vectorizer = CountVectorizer(stop_words="english")
X = vectorizer.fit_transform(documents + [query])  # Fit and transform the documents and query
vectors = X.toarray()  # Convert to array form

# Separate document vectors and query vector
doc_vectors = vectors[:-1]  # Documents only
query_vector = vectors[-1]  # Query only

# Function to compute distances
def compute_distances(doc_vectors, query_vector):
    euclidean_distances = [euclidean(doc, query_vector) for doc in doc_vectors]
    manhattan_distances = [cityblock(doc, query_vector) for doc in doc_vectors]
    cosine_similarities = cosine_similarity(doc_vectors, query_vector.reshape(1, -1)).flatten()
    return euclidean_distances, manhattan_distances, cosine_similarities

# Compute distances
euclidean_distances, manhattan_distances, cosine_similarities = compute_distances(doc_vectors, query_vector)

# Rank documents based on distances
euclidean_ranking = np.argsort(euclidean_distances)  # More distance, unlikely related
manhattan_ranking = np.argsort(manhattan_distances)  # More distance, unlikely related
cosine_ranking = np.argsort(-cosine_similarities)  # More cosine value, likely related

# Best 2 documents (+1 since indexing is from 0)
top_2_euclidean = euclidean_ranking[:2] + 1
top_2_manhattan = manhattan_ranking[:2] + 1
top_2_cosine = cosine_ranking[:2] + 1

# Output results
print("Euclidean Distance:", euclidean_distances)
print("Manhattan Distance:", manhattan_distances)
print("Cosine Similarity:", cosine_similarities)
print("\nTop 2 documents using Euclidean distance:", top_2_euclidean)
print("Top 2 documents using Manhattan distance:", top_2_manhattan)
print("Top 2 documents using Cosine similarity:", top_2_cosine)

# Output:
# Euclidean Distance: [2.0, 2.0, 1.7320508075688772, 1.7320508075688772, 2.0]
# Manhattan Distance: [4, 4, 3, 3, 4]
# Cosine Similarity: [0.33333333 0.65465367 0.57735027 0.70710678 0.51639778]

# Top 2 documents using Euclidean distance: [3 4]
# Top 2 documents using Manhattan distance: [3 4]
# Top 2 documents using Cosine similarity: [4 2]