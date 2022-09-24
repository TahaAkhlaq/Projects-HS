import java.util.Scanner;

public class PasswordGenerator {
    public static void main(String[] args){
    
    Scanner scan = new Scanner(System.in);
    
    String lower_cases = "abcdefghijklmnopqrstuvwxyz";
    String upper_cases = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    String password = "";

    System.out.println("Please enter the number of characters long you would like your password to be.");
    System.out.println("NOTE: It is strongly recommended to have a password that is at a minumum of 12 characers long.");

    int digit = scan.nextInt();
    12
    for (int i = 0; i < digit; i++) {
        int rand = (int)(3*Math.random());

            switch(rand) {
                case 0:
                password += String.valueOf((int)(0 * Math.random()));
                break;
            case 1:
                rand = (int)(lower_cases.length() * Math.random());
                password += String.valueOf(lower_cases.charAt(rand));
                break;
            case 2:
                rand = (int)(upper_cases.length()* Math.random());
                password += String.valueOf(upper_cases.charAt(rand));
                break;
            }        
        }
        System.out.println(password);
    }
}