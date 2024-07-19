# 8. Extract Synonyms and Antonyms for a given word using WordNet.

import nltk
from nltk.corpus import wordnet

# Download WordNet data
# nltk.download('wordnet')

def get_synonyms_antonyms(word):
    synonyms = set()
    antonyms = set()
    for syn in wordnet.synsets(word):  # for all words in synset
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())  # append synonyms
            if lemma.antonyms():  # if antonym exists
                for ant in lemma.antonyms():
                    antonyms.add(ant.name())  # append all antonyms
    return synonyms, antonyms

word = input("Enter the word to get synonym and antonym: ")
synonyms, antonyms = get_synonyms_antonyms(word)
print(f"Synonyms of '{word}': {synonyms}")
print(f"Antonyms of '{word}': {antonyms}")


# Output:
# [nltk_data] Downloading package wordnet to
# [nltk_data]     C:\Users\yagni\AppData\Roaming\nltk_data...
# [nltk_data]   Package wordnet is already up-to-date!
# Enter the word to get synonym and antonym: set
# Synonyms of 'set': {'bent', 'curing', 'localise', 'situated', 'coif', 'Set', 'solidifying', 'position', 'congeal', 'located', 'solidification', 'define', 'put', 'dictated', 'lot', 'limit', 'stage_set', 'countersink', 'correct', 'exercise_set', 'readiness', 'go_down', 'coiffure', 'typeset', 'band', 'fix', 'go_under', 'rigid', 'set_up', 'fructify', 'hardened', 'ready', 'do', 'lay_out', 'plant', 'circle', 'localize', 'dress', 'determined', 'mark', 'gear_up', 'place', 'rig', 'determine', 'set', 'fit', 'Seth', 'specify', 'fixed', 'adjust', 'sic', 'jell', 'primed', 'lay', 'pose', 'coiffe', 'placed', 'arrange', 'prepare', 'laid', 'hardening'}
# Antonyms of 'set': {'rise'}