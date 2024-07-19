// 2. Find the bigram count for the given corpus. Apply Laplace smoothing and find the bigram probabilities after add-one smoothing (up to 4 decimal places)

#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <map>
using namespace std;

int main() {
    int count;
    cout << "Enter the number of sentences in the corpus: ";
    cin >> count;
    cin.ignore();

    vector<string> corpus(count); // dataset (corpus)
    cout << "Enter the sentences for the corpus:" << endl;
    for (int i = 0; i < count; i++) {
        cout << "Sentence " << i + 1 << ": ";
        getline(cin, corpus[i]);
    }

    cout << "Enter the test sentence: ";
    string test; // test sentence
    getline(cin, test);
    stringstream test_ss(test);

    vector<string> test_words; // set of words in test sentence
    string word;
    while (test_ss >> word) {
        test_words.push_back(word); // tokenization
    }

    map<string, int> unigram;
    map<pair<string, string>, int> bigram;

    for (const auto& sentence : corpus) {
        stringstream ss(sentence);
        string prev_word;
        ss >> prev_word; // Read the first word
        unigram[prev_word]++; // Count the first word of each sentence
        string current_word;
        while (ss >> current_word) {
            unigram[current_word]++; // unigram addition
            bigram[{prev_word, current_word}]++; // bigram addition
            prev_word = current_word; // prev word for the bigram
        }
    }

    // Compute vocab size
    int vocab_size = unigram.size();

    // Display unigram counts
    cout << "\nUnigram Counts:" << endl;
    for (const auto& entry : unigram) {
        cout << entry.first << ": " << entry.second << endl;
    }

    // Display bigram counts
    cout << "\nBigram Counts:" << endl;
    for (const auto& entry : bigram) {
        cout << "(" << entry.first.first << ", " << entry.first.second << "): " << entry.second << endl;
    }

    // Compute probabilities for test sentence
    float probability = 1.0;
    cout << "\nBigram Probabilities:" << endl;
    for (size_t i = 0; i < test_words.size() - 1; i++) {
        string w1 = test_words[i];
        string w2 = test_words[i + 1];
        int bigram_count = bigram[{w1, w2}];
        int unigram_count = unigram[w1];
        float bigram_probability = (float)(bigram_count + 1) / (unigram_count + vocab_size);
        probability *= bigram_probability;
        cout << "(" << w1 << ", " << w2 << "): " << bigram_probability << endl;
    }

    cout << "\nOverall Probability: " << probability << endl;
    return 0;
}


//Output:
// Enter the number of sentences in the corpus: 3
// Enter the sentences for the corpus:
// Sentence 1: There is a big garden 
// Sentence 2: Children play in a garden
// Sentence 3: They play inside beautiful garden
// Enter the test sentence: They play in a big Garden

// Unigram Counts:
// Children: 1
// There: 1
// They: 1
// a: 2
// beautiful: 1
// big: 1
// garden: 3
// in: 1
// inside: 1
// is: 1
// play: 2

// Bigram Counts:
// (Children, play): 1
// (There, is): 1
// (They, play): 1
// (a, big): 1
// (a, garden): 1
// (beautiful, garden): 1
// (big, garden): 1
// (in, a): 1
// (inside, beautiful): 1
// (is, a): 1
// (play, in): 1
// (play, inside): 1

// Bigram Probabilities:
// (They, play): 0.166667
// (play, in): 0.153846
// (in, a): 0.166667
// (a, big): 0.153846
// (big, Garden): 0.0833333

// Overall Probability: 5.47885e-005