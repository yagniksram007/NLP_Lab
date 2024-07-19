#Extract synonyms and antonyms for a given word using wordnet

# nltk.download('wordnet')
# nltk.download('omw-1.4')

import nltk
from nltk.corpus import wordnet

def get_synonyms_antonyms(word):
    synonyms = set()
    antonyms = set()
    
    for syn in wordnet.synsets(word): # for all words in synset
        for lemma in syn.lemmas():
            synonyms.add(lemma.name()) #append synonyms
            if lemma.antonyms(): #if antonym exist
                for ant in lemma.antonyms():
                    antonyms.add(ant.name()) #append all antonyms
    
    return synonyms, antonyms

word = input("Enter the word to get synonym and antonym: ")
synonyms, antonyms = get_synonyms_antonyms(word)
print(f"Synonyms of '{word}': {synonyms}")
print(f"Antonyms of '{word}': {antonyms}")

# Output:
# Enter the word to get synonym and antonym: set
# Synonyms of 'set': {'fit', 'coif', 'mark', 'position', 'set', 'solidification', 'fix', 'go_down', 'specify', 'adjust', 'go_under', 'dress', 'Set', 'place', 'lay_out', 'do', 'hardening', 'prepare', 'coiffe', 'lay', 'situated', 'gear_up', 'plant', 'stage_set', 'hardened', 'arrange', 'solidifying', 'rig', 'jell', 'fixed', 'laid', 'determined', 'sic', 'localize', 'circle', 'Seth', 'localise', 'curing', 'fructify', 'typeset', 'congeal', 'correct', 'dictated', 'exercise_set', 'primed', 'band', 'placed', 'coiffure', 'readiness', 'bent', 'put', 'pose', 'lot', 'determine', 'countersink', 'rigid', 'located', 'set_up', 'define', 'limit', 'ready'}
# Antonyms of 'set': {'rise'}