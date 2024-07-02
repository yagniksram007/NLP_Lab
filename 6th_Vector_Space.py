# The dataset contains following 5 documents.
# D1: "Shipment of gold damaged in a fire"
# D2: "Delivery of silver arrived in a silver truck"
# D3. "Shipment of gold arrived in a track"
# D4: "Purchased silver and gold arrived in a wooden track"
# D5: "The arrival of gold and silver shipment is delayed."
# Find the top two relevant documents for the query document with the content "gold silver truck" wing the vector space model.
# Use the following similarity measure and analyze the result.
# a) Euclidean distance 
# b) Manhattan distance
# c) Cosine similarity

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import euclidean_distances, manhattan_distances, cosine_similarity

# Sample documents
documents = [
    "Shipment of gold damaged in a fire",
    "Delivery of silver arrived in a silver truck",
    "Shipment of gold arrived in a track",
    "Purchased silver and gold arrived in a wooden track",
    "The arrival of gold and silver shipment is delayed."
]

# Query document
query = "gold silver truck"

# Vectorize the documents and the query using TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents + [query])

# Convert the TF-IDF matrix to a dense array
tfidf_array = tfidf_matrix.toarray()

# Separate the query vector from the document vectors
query_vector = tfidf_array[-1]
document_vectors = tfidf_array[:-1]

# Calculate Euclidean distance
euclidean_dist = euclidean_distances(document_vectors, query_vector.reshape(1, -1)).flatten()

# Calculate Manhattan distance
manhattan_dist = manhattan_distances(document_vectors, query_vector.reshape(1, -1)).flatten()

# Calculate Cosine similarity
cosine_sim = cosine_similarity(document_vectors, query_vector.reshape(1, -1)).flatten()

# Create a DataFrame to store the distances and similarity
df = pd.DataFrame({
    'Document': ['D1', 'D2', 'D3', 'D4', 'D5'],
    'Euclidean Distance': euclidean_dist,
    'Manhattan Distance': manhattan_dist,
    'Cosine Similarity': cosine_sim
})

# Sort the DataFrame by each measure and get the top 2 relevant documents
top2_euclidean = df.sort_values(by='Euclidean Distance').head(2)
top2_manhattan = df.sort_values(by='Manhattan Distance').head(2)
top2_cosine = df.sort_values(by='Cosine Similarity', ascending=False).head(2)

# Display the results
print("Top 2 relevant documents based on Euclidean Distance:\n", top2_euclidean)
print("\nTop 2 relevant documents based on Manhattan Distance:\n", top2_manhattan)
print("\nTop 2 relevant documents based on Cosine Similarity:\n", top2_cosine)

# Output:
# Top 2 relevant documents based on Euclidean Distance:
#    Document  Euclidean Distance  Manhattan Distance  Cosine Similarity
# 1       D2            0.908190            2.223251           0.587595
# 3       D4            1.226811            3.442776           0.247468

# Top 2 relevant documents based on Manhattan Distance:
#    Document  Euclidean Distance  Manhattan Distance  Cosine Similarity
# 1       D2            0.908190            2.223251           0.587595
# 3       D4            1.226811            3.442776           0.247468

# Top 2 relevant documents based on Cosine Similarity:
#    Document  Euclidean Distance  Manhattan Distance  Cosine Similarity
# 1       D2            0.908190            2.223251           0.587595
# 3       D4            1.226811            3.442776           0.247468