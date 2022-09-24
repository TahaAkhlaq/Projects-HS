import java.util.Scanner;

class PasswordGenerator{
public static void main(String[] args){ 
    
    Scanner scan = new Scanner(System.in);

    String lower_cases = "abcdefghijklmnopqrstuvwxyz";
    String upper_cases = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    String symbols = "!@#$%^&*()?/";

    String password = "";

    System.out.println("Please enter the number of passwords you would like to generate.");
    int numberOfPasswords = scan.nextInt();

    System.out.println("Please enter the number of characters long you would like your password(s) to be.");
    System.out.println("NOTE: It is strongly recommended to have a password that is at a minimum of 12 characters long.");
    int charactersInPassword = scan.nextInt();

    for (int i = 0; i < charactersInPassword; i++) {
        int rand = (int)(3 * Math.random());

            switch(rand) {
                case 0:
                    password += String.valueOf((int)(0 * Math.random()));
                    break;

                case 1:
                    rand = (char)(lower_cases.length() * Math.random());
                    password += String.valueOf(lower_cases.charAt(rand));
                    break;

                case 2:
                    rand = (char)(upper_cases.length() * Math.random());
                    password += String.valueOf(upper_cases.charAt(rand));
                    break;

                case 3:
                    rand = (char)(symbols.length() * Math.random());
                    password += String.valueOf(symbols.charAt(rand));
                    break;
            }        
        }
    System.out.println(password);
    }
}