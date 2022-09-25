import java.util.Scanner;

class PasswordGenerator{
public static void main(String[] args){ 
    
    Scanner scan = new Scanner(System.in);

    // Declare Variables 
    String lowerCase = "abcdefghijklmnopqrstuvwxyz";
    String upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    String symbols = "<>,.{}[]+=-_!@#$%^&*()?/";

    String password = "";

    //Text
    System.out.println("Please enter the number of passwords you would like to generate: ");
    int numberOfPasswords = scan.nextInt();

    System.out.println();
    System.out.println("Please Enter the Number of Characters you would like in your Password(s): ");
    System.out.println("\033[3m   NOTE: It is Recommended that Passwords be at a Minimum of 16 Characters in Length.\033[0m");
    System.out.println("\033[3m   NOTE: Supported Character Length by the Password Generator is 8-128. \033[0m");
    int charactersInPassword = scan.nextInt();

    if (charactersInPassword < 8){
        System.out.println();
        System.out.println("Please Enter A Higher Character Length: ");
        }
    
    if (charactersInPassword > 128){
        System.out.println("Please Enter A Lower Character Length: ");
        }

    //Print Multiple Passwords and Correct Character Length
    System.out.println();
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
    
    }
}