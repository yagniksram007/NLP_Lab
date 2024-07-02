# nltk.download('wordnet')
# nltk.download('omw-1.4')

import nltk
from nltk.corpus import wordnet

def get_synonyms_antonyms(word):
    synonyms = []
    antonyms = []

    for syn in wordnet.synsets(word):
        # Filter synsets that are related to the desired meaning of "hero"
        if 'person' in syn.definition() or 'hero' in syn.definition():
            for lemma in syn.lemmas():
                synonyms.append(lemma.name())
                if lemma.antonyms():
                    antonyms.append(lemma.antonyms()[0].name())

    synonyms = set(synonyms)
    antonyms = set(antonyms)

    return synonyms, antonyms

word = input("Enter a word: ")
synonyms, antonyms = get_synonyms_antonyms(word)

print(f"Synonyms of '{word}': {synonyms}")
print(f"Antonyms of '{word}': {antonyms}")
