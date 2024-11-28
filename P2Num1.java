// This program converts letter grades to their equivalent GPA values and handles invalid inputs.
// It prompts the user to input 5 letter grades, and for each grade, it outputs the corresponding GPA value.
// If the grade entered is invalid, it prints an error message.

import java.util.Scanner;

public class P2Num1 {

    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);  // Create a scanner object to read user input

        for (int i = 0; i < 5; i++) {  // Loop to gather 5 inputs
            double grade;  
            System.out.println("Enter a letter grade ");
            String letterGrade = scnr.next().toUpperCase(); // Convert the letter to an uppercase string 

            if (letterGrade.equals("A")) {  // If the grade is an A, set grade to 4.0
                grade = 4.0;
            } else if (letterGrade.equals("B")) { // If the grade is a B, set grade to 3.0
                grade = 3.0;
            } else if (letterGrade.equals("C")) { // If the grade is a C, set grade to 2.0
                grade = 2.0;
            } else if (letterGrade.equals("D")) { // If the grade is a D, set grade to 1.0
                grade = 1.0;
            } else if (letterGrade.equals("F")) { // If the grade is an F, set grade to 0.0
                grade = 0.0;
            } else { // If the grade isn't a valid letter, print an error message and continue to the next iteration
                grade = 0.0;
                System.out.println("The letter grade is " + letterGrade + ", which is an error");
                continue;
            }

            // Output the final message telling us what the letter grade we entered is in GPA
            System.out.println("The letter grade is " + letterGrade + ", which is " + grade); 
        } // end of for loop

    } // end main 
}
