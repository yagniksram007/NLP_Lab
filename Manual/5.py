# 5. Given the following short movie reviews, each labeled with a genre, either comedy or action:
# a. fun, couple, love, love : comedy
# b. fast, furious, shoot : action
# c. couple, fly, fast, fun, fun :comedy
# d. furious, shoot, shoot, fun :action
# e. fly, fast, shoot, love :action
# and a new document D: fast, couple, shoot, fly
# compute the most likely class for D. Assume a naive Bayes classifier and use add-1 smoothing for the likelihoods.

from collections import defaultdict, Counter
import math

reviews = [
    ("fun, couple, love, love", "comedy"),
    ("fast, furious, shoot", "action"),
    ("couple, fly, fast, fun, fun", "comedy"),
    ("furious, shoot, shoot, fun", "action"),
    ("fly, fast, shoot, love", "action")
]  # define reviews

D = "fast, couple, shoot, fly"  # the query

def tokenize(text):
    return text.split(", ")  # split into words

class_docs = defaultdict(list)  # tokens based on class
vocabulary = set()  # vocab set (no repetitions)
class_count = defaultdict(int)

for review, category in reviews:  # classifying into classes
    tokens = tokenize(review)  # tokenization
    class_docs[category].extend(tokens)  # add tokens to respective class
    class_count[category] += 1  # increment the class count
    vocabulary.update(tokens)  # update the vocab set

vocab_size = len(vocabulary)
total_docs = len(reviews)

# prior probability calculation for each class
priors = {category: count / total_docs for category, count in class_count.items()}

likelihoods = {}
for category, tokens in class_docs.items():  # calculating likelihood probability for each class
    token_counts = Counter(tokens)
    total_words = len(tokens)
    likelihoods[category] = {
        word: (token_counts[word] + 1) / (total_words + vocab_size) for word in vocabulary
    }  # laplace smoothing

tokens = tokenize(D)  # tokenize the query document
posteriors = {}
for category in priors:  # calculating posterior probability for each class
    log_prob = math.log(priors[category])
    for token in tokens:
        log_prob += math.log(likelihoods[category].get(token, 1 / (len(class_docs[category]) + vocab_size)))
    posteriors[category] = log_prob

most_likely_class = max(posteriors, key=posteriors.get)

print('Posterior Probability:', posteriors)
print(f"The most likely class for the document '{D}' is: {most_likely_class}")

# Output:
# Posterior Probability: {'comedy': -9.52173897104528, 'action': -8.671115273688494}
# The most likely class for the document 'fast, couple, shoot, fly' is: action