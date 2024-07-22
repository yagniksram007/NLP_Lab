/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package p2;
import java.util.Scanner;

/**
 *
 * @author SAHYADRI
 */

public class P2 {

    public static int countBigrams(String[] corpus, String word1, String word2) {
       int count = 0;
       for (String sentence : corpus) {
           String[] words = sentence.split(" ");
           for (int i = 0; i < words.length - 1; i++) {
               if (word1.equalsIgnoreCase(words[i]) && word2.equalsIgnoreCase(words[i + 1])) {
                   count++;
               }
           }
       }
       return count;
   }

   public static int countUnigrams(String[] corpus, String word) {
       int count = 0;
       for (String sentence : corpus) {
           for (String w : sentence.split(" ")) {
               if (word.equalsIgnoreCase(w)) {
                   count++;
               }
           }
       }
       return count;
   }
 
   public static void main(String[] args) {
       
       // intialise scanner
       Scanner scanner = new Scanner(System.in);
       
       System.out.println("Enter n: ");
       int n = scanner.nextInt();
       
       scanner.nextLine();
       
       String[] corpus = new String[n];
       System.out.println("Enter corus: ");
       for (int i=0; i<n; i++ )
       {
           System.out.println("Sentence " +(i+1)+": ");
           corpus[i] = scanner.nextLine();
       }
      

       System.out.println("Enter test case: ");
       String testCase = scanner.nextLine();
       String[] testWords = testCase.split(" ");
       
       
       double probability = 1;
       int corpusSize = 0;

       for (int i = 0; i < testWords.length - 1; i++) {
           probability *= (double) countBigrams(corpus, testWords[i], testWords[i + 1])
                   / (countUnigrams(corpus, testWords[i]) + corpusSize);
       }

       System.out.printf("Probability: %f%n", probability*100000);
   }
}