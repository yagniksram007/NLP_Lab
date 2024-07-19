//Find the bigram count for the given corpus. 
//Apply laplace smoothing and find the bigram probablities after add-one smoothing(upto 4 decimal places)

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_WORDS 100
#define MAX_WORD_LEN 50
#define ALPHA 1  // Laplace smoothing factor

// Function to tokenize the text and store words in an array
int tokenize(char *str, char words[MAX_WORDS][MAX_WORD_LEN]) {
    int i = 0;
    char *token = strtok(str, " .");
    while (token != NULL && i < MAX_WORDS) {
        strcpy(words[i], token);
        i++;
        token = strtok(NULL, " .");
    }
    return i;
}

// Function to find the bigram count with Laplace smoothing
void bigramCount(char words[MAX_WORDS][MAX_WORD_LEN], int wordCount) {
    int bigramCounts[MAX_WORDS][MAX_WORDS] = {0};
    int unigramCounts[MAX_WORDS] = {0};
    int vocabularySize = 0;
    char vocabulary[MAX_WORDS][MAX_WORD_LEN];

    // Create the vocabulary and count unigrams
    for (int i = 0; i < wordCount; i++) {
        int found = 0;
        for (int j = 0; j < vocabularySize; j++) {
            if (strcmp(words[i], vocabulary[j]) == 0) {
                unigramCounts[j]++;
                found = 1;
                break;
            }
        }
        if (!found) {
            strcpy(vocabulary[vocabularySize], words[i]);
            unigramCounts[vocabularySize]++;
            vocabularySize++;
        }
    }

    // Count bigrams
    for (int i = 0; i < wordCount - 1; i++) {
        int word1Index = -1, word2Index = -1;
        for (int j = 0; j < vocabularySize; j++) {
            if (strcmp(words[i], vocabulary[j]) == 0) word1Index = j;
            if (strcmp(words[i + 1], vocabulary[j]) == 0) word2Index = j;
        }
        if (word1Index != -1 && word2Index != -1) {
            bigramCounts[word1Index][word2Index]++;
        }
    }

    // Print bigram probabilities with add-one smoothing
    printf("Bigram probabilities with add-one smoothing:\n");
    for (int i = 0; i < vocabularySize; i++) {
        for (int j = 0; j < vocabularySize; j++) {
            double probability = (double)(bigramCounts[i][j] + ALPHA) / (unigramCounts[i] + ALPHA * vocabularySize);
            printf("P(%s|%s) = %.4f\n", vocabulary[j], vocabulary[i], probability);
        }
    }
}

int main() {
    char corpus[] = "There is a big garden. Children play in garden. They play inside beautiful garden.";
    char sentence[] = "They play in a big garden.";
    char words[MAX_WORDS][MAX_WORD_LEN];
    int wordCount;

    wordCount = tokenize(corpus, words);
    bigramCount(words, wordCount);

    return 0;
}
