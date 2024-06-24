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

# Top-down parser (RecursiveDescentParser)
print("Top-down Parsing (Recursive Descent):")
rd_parser = nltk.RecursiveDescentParser(grammar, trace=2)
for tree in rd_parser.parse(tokens):
    print(tree)
    tree.draw()

# Bottom-up parser (ShiftReduceParser)
print("\nBottom-up Parsing (Shift-Reduce):")
sr_parser = nltk.ShiftReduceParser(grammar, trace=2)
for tree in sr_parser.parse(tokens):
    print(tree)
    tree.draw()
