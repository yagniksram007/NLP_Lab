#include <stdio.h>
void main()
{
    int n,i;
    
    // Taking limit
    printf("Enter the no. of sentences: ");
    scanf("%d",&n);

     // Clear input buffer
    while (getchar() != '\n');

    // Array to store the sentences
    char sentences[n][100];

    // Read n sentences from the user
    printf("Enter %d sentences:\n", n);
    for (int i = 0; i < n; i++) {
        printf("Sentence %d: ", i + 1);
        fgets(sentences[i], sizeof(sentences[i]), stdin);
    }


    // Display the entered sentences
    printf("\nEntered sentences:\n");
    for (int i = 0; i < n; i++) {
        printf("%s", sentences[i]);
    }


}