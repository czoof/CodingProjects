import java.util.Scanner;

public class H5B {
    public static void main(String[] args) {

        //get booleans
        boolean validDay = true;
        boolean validMonth = true;
        boolean validYear = true;
                
        //Get input from keyboard
        Scanner keyboard = new Scanner(System.in);
        System.out.println("Enter a date in the form mm/dd/yyyy");
        String userInput = keyboard.next();
        
        //Find the first slash and extract the month
        int subForMonth = userInput.indexOf("/");
        String month = userInput.substring(0, subForMonth); 
        
        //Extract the day part by finding the second slash
        String restOfDate = userInput.substring(subForMonth + 1);
        int subForDay = restOfDate.indexOf("/");
        String day = restOfDate.substring(0, subForDay); 
        
        // Extract the year part
        String year = restOfDate.substring(subForDay + 1); 

        //Convert date to int
        int monthAsInt = Integer.parseInt(month);
        int dayAsInt = Integer.parseInt(day);
        int yearAsInt = Integer.parseInt(year);

        //Check if the year is valid
        if (yearAsInt >= 1700 && yearAsInt <= 2100) {
            validYear = true;
        } 
        else {
            validYear = false;
        }

        //Check if the month is valid
        if (monthAsInt >= 1 && monthAsInt <= 12) {
            validMonth = true;
        } 
        else {
            validMonth = false;
        }

        //Check valid days for months with 31 days
        if (monthAsInt == 1 || monthAsInt == 3 || monthAsInt == 5 || monthAsInt == 7 || monthAsInt == 8 || monthAsInt == 10 || monthAsInt == 12) {
            if (dayAsInt < 1 || dayAsInt > 31) {
                validDay = false;
            }
        }
        //Check valid days for months with 30 days
        else if (monthAsInt == 4 || monthAsInt == 6 || monthAsInt == 9 || monthAsInt == 11) {
            if (dayAsInt < 1 || dayAsInt > 30) {
                validDay = false;
            }
        }
        
        //find leap year
        else if (monthAsInt == 2) {
            if ((yearAsInt % 4 == 0 && yearAsInt % 100 != 0) || (yearAsInt % 400 == 0)) {
                if (dayAsInt < 1 || dayAsInt > 29) {
                    validDay = false;
                }
            } 
            else {
                if (dayAsInt < 1 || dayAsInt > 28) {
                    validDay = false;
                }
            }
        }

        //output valid date if year month and day are all true
        if (validYear && validMonth && validDay) {
            System.out.println("Valid Date");
        } else {
            System.out.println("Invalid Date");
        }
        keyboard.close();



    }//end main
}