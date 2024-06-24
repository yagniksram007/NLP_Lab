import nltk

# Define the grammar
grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Adj N
    VP -> V NP | V
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat' | 'man' | 'telescope'
    V -> 'saw' | 'ate' | 'walked'
    Adj -> 'big' | 'small'
""")

# Define the sentence to parse
sentence = "the man saw a small dog"
tokens = sentence.split()

# Create the bottom-up parser
parser = nltk.ShiftReduceParser(grammar, trace =2)

tree = list(parser.parse(tokens))

# Parse the sentence
for tree in parser.parse:
    print(tree)