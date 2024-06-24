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
    return max(posteriors, key=posteriors.get)

# Classify the new document
most_likely_class = classify(D)
print(f"The most likely class for '{D}' is '{most_likely_class}'.")