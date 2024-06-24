//Consider the following corpus of three statments
//a. There is a big garden. 
//b. Children play in garden. 
//c. They play inside beautiful garden.

// Calculate P for the sentence 'They play in a big garden' assuming a bigram language model 

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_WORDS 100
#define MAX_WORD_LEN 50
#define VOCAB_SIZE 20  // Adjust this based on the vocabulary size in the corpus

// Function to tokenize the input string
int tokenize(char *str, char tokens[MAX_WORDS][MAX_WORD_LEN]) {
    int i = 0;
    char *token = strtok(str, " ");
    while (token != NULL && i < MAX_WORDS) {
        strcpy(tokens[i], token);
        i++;
        token = strtok(NULL, " ");
    }
    return i;
}

// Function to find the index of a word in the vocabulary
int find_index(char vocab[VOCAB_SIZE][MAX_WORD_LEN], int vocab_size, char *word) {
    for (int i = 0; i < vocab_size; i++) {
        if (strcmp(vocab[i], word) == 0) {
            return i;
        }
    }
    return -1;
}

// Function to compute bigram probabilities with Laplace smoothing
void compute_bigram_probabilities(char tokens[MAX_WORDS][MAX_WORD_LEN], int num_tokens, 
                                  double bigram_probs[VOCAB_SIZE][VOCAB_SIZE], char vocab[VOCAB_SIZE][MAX_WORD_LEN]) {
    int unigram_counts[VOCAB_SIZE] = {0};
    int bigram_counts[VOCAB_SIZE][VOCAB_SIZE] = {0};
    int vocab_size = 0;

    // Build the vocabulary and count unigrams
    for (int i = 0; i < num_tokens; i++) {
        int index = find_index(vocab, vocab_size, tokens[i]);
        if (index == -1) {
            strcpy(vocab[vocab_size], tokens[i]);
            unigram_counts[vocab_size]++;
            vocab_size++;
        } else {
            unigram_counts[index]++;
        }
    }

    // Count bigrams
    for (int i = 0; i < num_tokens - 1; i++) {
        int index1 = find_index(vocab, vocab_size, tokens[i]);
        int index2 = find_index(vocab, vocab_size, tokens[i + 1]);
        if (index1 != -1 && index2 != -1) {
            bigram_counts[index1][index2]++;
        }
    }

    // Compute bigram probabilities with Laplace smoothing
    for (int i = 0; i < vocab_size; i++) {
        for (int j = 0; j < vocab_size; j++) {
            bigram_probs[i][j] = (double)(bigram_counts[i][j] + 1) / (unigram_counts[i] + vocab_size);
        }
    }
}

// Function to calculate the probability of a sentence
double sentence_probability(char *sentence, double bigram_probs[VOCAB_SIZE][VOCAB_SIZE], 
                            char vocab[VOCAB_SIZE][MAX_WORD_LEN], int vocab_size) {
    char tokens[MAX_WORDS][MAX_WORD_LEN];
    int num_tokens = tokenize(sentence, tokens);
    double probability = 1.0;

    for (int i = 0; i < num_tokens - 1; i++) {
        int index1 = find_index(vocab, vocab_size, tokens[i]);
        int index2 = find_index(vocab, vocab_size, tokens[i + 1]);
        if (index1 != -1 && index2 != -1) {
            probability *= bigram_probs[index1][index2];
        } else {
            probability = 0;
            break;
        }
    }
    return probability;
}

int main() {
    char corpus[] = "There is a big garden. Children play in garden. They play inside beautiful garden.";
    char tokens[MAX_WORDS][MAX_WORD_LEN];
    int num_tokens = tokenize(corpus, tokens);

    double bigram_probs[VOCAB_SIZE][VOCAB_SIZE];
    char vocab[VOCAB_SIZE][MAX_WORD_LEN];

    compute_bigram_probabilities(tokens, num_tokens, bigram_probs, vocab);

    char sentence[] = "They play in a big garden.";
    double prob = sentence_probability(sentence, bigram_probs, vocab, VOCAB_SIZE);

    printf("Probability of the sentence '%s' is %.4f\n", sentence, prob);

    return 0;
}

// Output:
// Probability of the sentence 'They' is 0.0001