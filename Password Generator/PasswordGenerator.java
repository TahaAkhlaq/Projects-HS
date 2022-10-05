import java.util.Scanner;

public class PasswordGenerator {
    public static void main(String[] args) {

        try (Scanner scan = new Scanner(System.in)) {
            // Initialize Variables
            String lowerCase = "abcdefghijklmnopqrstuvwxyz";
            String upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            String symbols = "<>,.{}[]+=-_!@#$%^&*()?/";

            String password = "";

            // Declare Variables
            String answer;

            do {
                // Text
                System.out.println("\nPlease Enter the number of Passwords you would like to Generate: ");
                int numberOfPasswords = scan.nextInt();

                System.out.println("\nPlease Enter the Number of Characters you would like in your Password(s): ");
                System.out.println("\033[3m   NOTE: It is Recommended that Passwords be at a Minimum of 16 Characters in Length.\033[0m");
                System.out.println("\033[3m   NOTE: Supported Character Length by the Password Generator is 8-128. \033[0m");
                int charactersInPassword = scan.nextInt();

                // Ensure The User Entered A Character Length Between 8 and 128
                while (charactersInPassword < 8 || charactersInPassword > 128) {
                    System.out.println("\nPlease Enter A Character Length Between 8-128: ");
                    charactersInPassword = scan.nextInt();
                }

                // Print Multiple Passwords and Correct Character Length
                System.out.println("\n\nPassword(s): ");
                for (int i = 0; i < numberOfPasswords; i++) {
                    password = "";

                    for (int j = 0; j < charactersInPassword; j++) {
                        int random = (int) (4 * Math.random());

                        switch (random) {
                            case 0:
                                password += String.valueOf((int) (10 * Math.random()));
                                break;

                            case 1:
                                random = (int) (upperCase.length() * Math.random());
                                password += String.valueOf(upperCase.charAt(random));
                                break;

                            case 2:
                                random = (int) (lowerCase.length() * Math.random());
                                password += String.valueOf(lowerCase.charAt(random));
                                break;

                            case 3:
                                random = (int) (symbols.length() * Math.random());
                                password += String.valueOf(symbols.charAt(random));
                                break;

                        }

                    }
                    System.out.println("\n" + password);

                }
                System.out.println("\n");

                // Password Strength
                if (charactersInPassword <= 7) {
                    System.out.println("Password Strength: WEAK\n");
                }

                else if (charactersInPassword >= 8 && charactersInPassword <= 11) {
                    System.out.println("Password Strength: STRONG\n");
                }

                else if (charactersInPassword >= 12 && charactersInPassword <= 15) {
                    System.out.println("Password Strength: VERY STRONG\n");
                }

                else if (charactersInPassword >= 16) {
                    System.out.println("Password Strength: EXTREMELY STRONG\n");
                }

                // Ask the User if they would like to Reuse the Password Generator
                System.out.println("\nWould you like to Reuse the Password Generator? (Yes or No)\n");
                answer = scan.next();
            } while (answer.equalsIgnoreCase("Yes"));
            {
                if (answer.equalsIgnoreCase("No")) {
                    System.out.println("\nThank you. Goodbye!\n");

                }
            }
        }

    }
}