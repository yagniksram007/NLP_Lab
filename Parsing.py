
#Implement top down and bottom up parsing using python NLTK

import nltk
from nltk import CFG

# Define a simple grammar
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP
    VP -> V NP | V NP PP
    PP -> P NP
    Det -> 'the' | 'a'
    N -> 'cat' | 'dog' | 'telescope' | 'park'
    V -> 'saw' | 'walked'
    P -> 'in' | 'with'
""")

# Define the sentence to be parsed
sentence = "the cat saw a dog".split()

# Top-Down Parsing using Recursive Descent Parser
def top_down_parsing(grammar, sentence):
    print("Top-Down Parsing (Recursive Descent):")
    parser = nltk.RecursiveDescentParser(grammar)
    for tree in parser.parse(sentence):
        print(tree)

# Bottom-Up Parsing using Shift-Reduce Parser
def bottom_up_parsing(grammar, sentence):
    print("Bottom-Up Parsing (Shift-Reduce):")
    parser = nltk.ShiftReduceParser(grammar)
    for tree in parser.parse(sentence):
        print(tree)

# Main function to run both parsers
def main():
    # Top-Down Parsing
    top_down_parsing(grammar, sentence)
    
    # Bottom-Up Parsing
    bottom_up_parsing(grammar, sentence)

if __name__ == "__main__":
    main()

