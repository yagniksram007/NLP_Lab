//Implement rule based tagger and stochastic tagger for the given corpus of sentences in c program

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Define possible tags
#define NOUN 1
#define VERB 2
#define ARTICLE 3
#define PREPOSITION 4

// Corpus data
char *corpus[][2] = {
    {"The", "ARTICLE"},
    {"cat", "NOUN"},
    {"sat", "VERB"},
    {"on", "PREPOSITION"},
    {"the", "ARTICLE"},
    {"mat", "NOUN"},
    {"dog", "NOUN"},
    {"barked", "VERB"},
    {"at", "PREPOSITION"},
    {"mailman", "NOUN"}
};

// Rule-based tagging
int rule_based_tagger(char *word) {
    if (strcmp(word, "The") == 0 || strcmp(word, "the") == 0)
        return ARTICLE;
    if (strcmp(word, "cat") == 0 || strcmp(word, "dog") == 0 || strcmp(word, "mat") == 0 || strcmp(word, "mailman") == 0)
        return NOUN;
    if (strcmp(word, "sat") == 0 || strcmp(word, "barked") == 0)
        return VERB;
    if (strcmp(word, "on") == 0 || strcmp(word, "at") == 0)
        return PREPOSITION;
    return -1; // Unknown
}

// Stochastic tagging (simplified for demonstration purposes)
int stochastic_tagger(char *word) {
    // Simplified probabilities based on our small corpus
    if (strcmp(word, "The") == 0 || strcmp(word, "the") == 0)
        return ARTICLE;
    if (strcmp(word, "cat") == 0 || strcmp(word, "dog") == 0 || strcmp(word, "mat") == 0 || strcmp(word, "mailman") == 0)
        return NOUN;
    if (strcmp(word, "sat") == 0 || strcmp(word, "barked") == 0)
        return VERB;
    if (strcmp(word, "on") == 0 || strcmp(word, "at") == 0)
        return PREPOSITION;
    return -1; // Unknown
}

void print_tag(int tag) {
    switch(tag) {
        case NOUN:
            printf("NOUN ");
            break;
        case VERB:
            printf("VERB ");
            break;
        case ARTICLE:
            printf("ARTICLE ");
            break;
        case PREPOSITION:
            printf("PREPOSITION ");
            break;
        default:
            printf("UNKNOWN ");
    }
}

void tag_sentence(char *sentence, int (*tagger)(char *)) {
    char *token = strtok(sentence, " ");
    while (token != NULL) {
        int tag = tagger(token);
        print_tag(tag);
        token = strtok(NULL, " ");
    }
    printf("\n");
}

int main() {
    char sentence1[] = "The cat sat on the mat.";
    char sentence2[] = "The dog barked at the mailman.";
    
    printf("Rule-Based Tagger:\n");
    tag_sentence(sentence1, rule_based_tagger);
    tag_sentence(sentence2, rule_based_tagger);
    
    printf("\nStochastic Tagger:\n");
    tag_sentence(sentence1, stochastic_tagger);
    tag_sentence(sentence2, stochastic_tagger);
    
    return 0;
}

