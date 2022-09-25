import java.util.Scanner;

class PasswordGenerator{
public static void main(String[] args){ 
    
    Scanner scan = new Scanner(System.in);

    // Declare Variables 
    String lowerCase = "abcdefghijklmnopqrstuvwxyz";
    String upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    String symbols = "<>,.{}[]+=-_!@#$%^&*()?/";

    String password = "";

    String answer;

    do {
        //Text
        System.out.println();
        System.out.println("Please Enter the number of Passwords you would like to Generate: ");
        int numberOfPasswords = scan.nextInt();

        System.out.println();
        System.out.println("Please Enter the Number of Characters you would like in your Password(s): ");
        System.out.println("\033[3m   NOTE: It is Recommended that Passwords be at a Minimum of 16 Characters in Length.\033[0m");
        System.out.println("\033[3m   NOTE: Supported Character Length by the Password Generator is 8-128. \033[0m");
        int charactersInPassword = scan.nextInt();


        //Ensure The User Entered A Character Length Between 8 and 128
        while (charactersInPassword < 8 || charactersInPassword > 128 ){
                System.out.println();
                System.out.println("Please Enter A Character Length Between 8-128: ");
                charactersInPassword = scan.nextInt();
                }
            

        //Print Multiple Passwords and Correct Character Length
        System.out.println();
        System.out.println();
        System.out.println("Password(s): ");
        for (int i = 0; i < numberOfPasswords; i++) {
            password ="";

        
                for (int j = 0; j < charactersInPassword; j++) {
                int random = (int)(4 * Math.random());

                switch(random) {
                    case 0:
                        password += String.valueOf((int)(10 * Math.random()));
                        break;
                
                    case 1:
                        random = (int)(upperCase.length() * Math.random());
                        password += String.valueOf(upperCase.charAt(random));
                        break;

                    case 2:
                        random = (int)(lowerCase.length() * Math.random());
                        password += String.valueOf(lowerCase.charAt(random));
                        break;

                    case 3:
                        random = (int)(symbols.length() * Math.random());
                        password += String.valueOf(symbols.charAt(random));
                        break;
                        
                    }
                
                }
                System.out.println();
                System.out.println(password);
                
            }
        System.out.println();
        System.out.println();


        //Password Strength
        if (charactersInPassword <= 7){
            System.out.println("Password Strength: WEAK");
            System.out.println();
            }

        if (charactersInPassword >= 8 && charactersInPassword <= 11 ){
            System.out.println("Password Strength: STRONG");
            System.out.println();
            }

        if (charactersInPassword >= 12 && charactersInPassword <= 15){
            System.out.println("Password Strength: VERY STRONG");
            System.out.println();
            }

        if (charactersInPassword >= 16){
            System.out.println("Password Strength: EXTREMELY STRONG");
            System.out.println();
            } 

        // Ask the User if they would like to Reuse the Password Generator
        System.out.println();
        System.out.println("Would you like to Reuse the Password Generator? (Yes or No)");
        System.out.println();
        answer = scan.next();
        }while (answer.equalsIgnoreCase("Yes")); {
            if (answer.equalsIgnoreCase("No")){
                System.out.println();
                System.out.println("Thank you. Goodbye!");
                System.out.println();
                }
            }
        
    }
}