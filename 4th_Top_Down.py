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

# Create the top-down parser
rd_parser = nltk.RecursiveDescentParser(grammar, trace = 2)

# Define the sentence to parse
sentence = "the man saw a small dog"
tokens = sentence.split()

trees = rd_parser.parse(tokens)

# Parse the sentence
for tree in trees:
    print(tree)
    tree.draw()