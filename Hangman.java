//hi.
//hangman
//get word
//make another string full of underlines eqivivlant to the length of word
//display guess
//initialize count
//user gets 10 guesses of a character. If word not guessed, they lose
//as long as the guess is correct, the number of guesses do not decrease
//loop max of 10 times
    //ask user for letter
    //get letter from keyboard
    //if letter not found, then increment count
    //if letter is found, then we go to the loop below
    //loop through characters in the word and check if any of them hit
        //if find letter at index i, replace character with letter
//end loop 2 //output guess so far
//end loop1

package hangman;
import java.io.File; //import file class to handle file input
import java.io.FileNotFoundException;  //import exception 
import java.util.Scanner; //import scanner for the main program
import java.util.Random; //import random scanner

public class Hangman {

    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        Random random = new Random(); //random to pick random word
        String word = ""; //initialize word variable
        String wordForGame = ""; //word for the game
        String displayWord = ""; //displayed word
        String guess = ""; //word for guess
        int count = 0;  
        int guesses = 10; //how many guesses we get
        boolean fetch = false; //boolean to check if guess is correct
        
        File file = new File("words_no_duplicates.txt"); //specify path of file

        try (Scanner scanner = new Scanner(file)) { //try with code to automatically close scanner after it is used
            while (scanner.hasNext()) { //while there is an input
                word = scanner.next(); //read the next word
                count++; 
                if (random.nextInt(count) == 0){  //finding where the word is at based on count
                    wordForGame = word;
                }
            }
            System.out.println("Welcome to hangman. Guess a letter");

            //initialize display word with underscores 
            for (int i = 0; i < wordForGame.length(); i++) {
                displayWord += "_";
            }

            while (guesses > 0) {  //main loop
                System.out.println("Current word: " + displayWord);
                System.out.print("Enter a letter: ");
                guess = scnr.next(); //getting each of our guesses

                if (guess.length() != 1) {  
                    System.out.println("Only enter one letter.");
                    continue; //continue if we don't guess a character
                }

                guess = guess.toLowerCase(); //convert guess to lower case
                fetch = false; //reset fetch flag before each guess
                
                //check if guessed letter is in the word
                for (int i = 0; i < wordForGame.length(); i++) { 
                    if (Character.toLowerCase(wordForGame.charAt(i)) == guess.charAt(0)) {
                        displayWord = displayWord.substring(0, i) + wordForGame.charAt(i) + displayWord.substring(i + 1);
                        fetch = true; //set boolean to true if guess is correct
                    }
                }

                if (!fetch) {  //if boolean is false, subtract from guesses
                    guesses--;
                    System.out.println("Wrong. You have " + guesses + " guesses left.");
                }

                if (!displayWord.contains("_")) {  //if no more underscores, user wins
                    System.out.println("You won! The word was: " + wordForGame);
                    break;
                }

                if (guesses == 0) { //if guesses = 0, user loses
                    System.out.println("You lost! The word was: " + wordForGame);
                }
            }
        } catch (FileNotFoundException e) { //catch block to handle file not found
            System.out.println("File not found: " + e.getMessage()); 
        }
    } //end main
} //end class

        
        
        
        
        
        
        
        
        
        
        
