//Find the bigram count for the given corpus. 
//Apply laplace smoothing and find the bigram probablities after add-one smoothing(upto 4 decimal places)

#include <stdio.h>
#include <string.h>

#define MAX_WORDS 100
#define MAX_WORD_LEN 50
#define VOCAB_SIZE 10  // Adjust this based on the vocabulary size in the corpus

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
void compute_bigram_probabilities(char tokens[MAX_WORDS][MAX_WORD_LEN], int num_tokens) {
    char vocab[VOCAB_SIZE][MAX_WORD_LEN];
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

    // Compute and print bigram probabilities with Laplace smoothing
    printf("Bigram Probabilities (with Laplace Smoothing):\n");
    for (int i = 0; i < vocab_size; i++) {
        for (int j = 0; j < vocab_size; j++) {
            double probability = (double)(bigram_counts[i][j] + 1) / (unigram_counts[i] + vocab_size);
            printf("P(%s|%s) = %.4f\n", vocab[j], vocab[i], probability);
        }
    }
}

int main() {
    char corpus[] = "the quick brown fox jumps over the lazy dog";
    char tokens[MAX_WORDS][MAX_WORD_LEN];
    int num_tokens = tokenize(corpus, tokens);

    compute_bigram_probabilities(tokens, num_tokens);

    return 0;
}

