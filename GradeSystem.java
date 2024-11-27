import java.util.Scanner;
public class P2Num1{
    
    public static void main(String[] args){
    Scanner scnr = new Scanner(System.in);  //get scanner

    for (int i=0; i<5; i++){  //initial for loop, lets us gather 5 inputs
        double grade;  
        System.out.println("Enter a letter grade ");
        String letterGrade = scnr.next().toUpperCase(); //convery the letter to an uppercase string 

        if (letterGrade.equals("A")){  //if the grade is an a, print out a 4.0
            grade = 4.0;
        }
        else if (letterGrade.equals("B")){//if the grade is a b, print out a 3.0
            grade = 3.0;
        }
        else if (letterGrade.equals("C")){//if the grade is a c, print out a 3.0
            grade = 2.0;
        }
        else if (letterGrade.equals("D")){//if the grade is a d, print out a 1.0
            grade = 1.0;
        }
        else if (letterGrade.equals("F")){//if the grade is an f, print out a 0.0
            grade = 0.0;
        }
        else{ //if the grade isnt a valid number, get an error message
            grade = 0.0;
            System.out.println("The letter grade is " + letterGrade + ", which is an error");
            continue;
        }

        System.out.println("The letter grade is " + letterGrade + ", which is " + grade); // output the final message telling us what the letter grade we entered is in gpa
    }// end of for loop


    }//end main 
}