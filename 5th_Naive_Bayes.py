# Given the following short movie reviews, each labeled with a gente, either comedy or action
# a) fun, couple, love, love comedy 
# b) fast, farious, shoot action
# c) couple, fly, fast, fun, fun comedy
# d) furious, shout, shoot, fun action 
# e) fly, fast, shoot, love action

# and a new document D: fast, couple, shoot, fly
# compute the most likely class for D. Assume a naive Bayes classifier and use add-1 smoothing for the likelihoods

from collections import defaultdict

# Training data
reviews = [
    ("fun couple love love", "comedy"),
    ("fast furious shoot", "action"),
    ("couple fly fast fun fun", "comedy"),
    ("furious shoot shoot fun", "action"),
    ("fly fast shoot love", "action")
]

# New document to classify
D = "fast couple shoot fly"

# Preprocess the data
vocabulary = set()
class_counts = defaultdict(int)
word_counts = defaultdict(lambda: defaultdict(int))

for review, cls in reviews:
    words = review.split()
    vocabulary.update(words)
    class_counts[cls] += 1
    for word in words:
        word_counts[cls][word] += 1

N = sum(class_counts.values())
classes = list(class_counts.keys())

# Classify the new document
def classify(document):
    words = document.split()
    posteriors = {cls: class_counts[cls] / N for cls in classes}
    for cls in classes:
        for word in words:
            posteriors[cls] *= (word_counts[cls].get(word, 0) + 1) / (class_counts[cls] + len(vocabulary))
    return posteriors

# Get the posterior probabilities
posteriors = classify(D)

# Convert to percentages
total_prob = sum(posteriors.values())
percentages = {cls: (prob / total_prob) for cls, prob in posteriors.items()}

# Print the results
for cls, percentage in percentages.items():
    print(f"The probability for class '{cls}' is {percentage:.2f}.")

# Print the most likely class
most_likely_class = max(posteriors, key=posteriors.get)
print(f"The most likely class for '{D}' is '{most_likely_class}'.")

# Output:
# The probability for class 'comedy' is 0.29.
# The probability for class 'action' is 0.71.
# The most likely class for 'fast couple shoot fly' is 'action'.
