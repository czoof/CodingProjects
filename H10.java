// Program to display different types of flowers, the total number of each flower sold, 
// and how many flowers each person sold.

// The program generates random numbers to represent how many flowers each person sold 
// for each type, organizes and displays this data in a tabular format, and calculates 
// the total flowers sold by each person and the total of each flower type

import java.util.Random;

public class H10 {
    public static void main(String[] args) {
        Random randgen = new Random();

        String[] flowerArray = {"petunia", "pansy", "rose", "violet", "carnation"}; // array for the names of the flowers
        String[] nameArray = {"Frankie", "Janet", "Sam", "Abbie"}; // array for the names of the people 
        int[][] flowers = new int[4][5]; // flowers array, the 4 represents the names of the people and the 5 represents the flower names
        int[] totalBuyer = new int[flowers.length]; // total array of the buyers
        int[] totalFlowers = new int[flowers[0].length]; // total array of the flowers

        int row, col;
        for (row = 0; row < 4; row++) {
            for (col = 0; col < 5; col++) {
                flowers[row][col] = randgen.nextInt(21); // for loop iterating over the rows and columns assigning random numbers to them
            }
        }

        for (int k = 0; k < 5; k++) {
            System.out.print("\t\t" + flowerArray[k]); // organizing the spacing of the flower words
        }
        System.out.println("");

        for (row = 0; row < 4; row++) {
            System.out.print(nameArray[row] + "\t\t"); // organizing the names of the people in the rows
            for (col = 0; col < 5; col++) {
                System.out.print(flowers[row][col] + "\t\t"); // organizing the numbers inside each row and column so it lines up properly with each other
            }
            System.out.println("");
        }

        for (int i = 0; i < flowers.length; i++) {
            for (int j = 0; j < flowers[i].length; j++) { // for loop iterating over the flowers and assigning the totals array and the total flowers array
                totalBuyer[i] += flowers[i][j];          // to calculate how many flowers each person bought, and the total of each flower inside the program.
                totalFlowers[j] += flowers[i][j];       // This eliminates the process of having to design a for loop for each and every total flower and total flowers that each buyer bought.
            }
            System.out.println(nameArray[i] + " sold " + totalBuyer[i] + " flowers"); // outputting each person's total flowers bought
        }

        for (int i = 0; i < totalFlowers.length; i++) {
            System.out.println("Total number of " + flowerArray[i] + " sold: " + totalFlowers[i]); // outputting the total of each of the different flowers in the program
        }

    } // end main
} // end class
