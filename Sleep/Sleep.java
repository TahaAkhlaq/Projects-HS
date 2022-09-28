
import java.util.Scanner;

public class Sleep {

    public static void main(String[] args) {

        try (Scanner scan = new Scanner(System.in)) {

            // Birthdate
            System.out.println("Enter your birthdate: ");
            System.out.print("Year: ");
            int birthYear = scan.nextInt();
            System.out.print("Month: ");
            int birthMonth = scan.nextInt();
            System.out.print("Day: ");
            int birthDay = scan.nextInt();

            // Current Date
            System.out.println("\nEnter today's date: ");
            System.out.print("Year: ");
            int todayYear = scan.nextInt();
            System.out.print("Month: ");
            int todayMonth = scan.nextInt();
            System.out.print("Day: ");
            int todayDay = scan.nextInt();

            /// Calculate the number of days
            int days = (todayYear - birthYear) * 365
                    + (todayMonth - birthMonth) * 30
                    + (todayDay - birthDay);

            // Calculate the number of hours asleep
            int hours = days * 8;

            // Display the results
            if (days >= 1000 && (days % 1000) < 100) {
                int d = 0;
                System.out.println("You have been alive for " + days / 1000 + "," + d + days % 1000 + " days.");

            } else if (days >= 1000)
                System.out.println("You have been alive for " + days / 1000 + "," + +days % 1000 + " days.");

            else if (days < 1)
                System.out.println("You have been alive for 0 days.");

            else
                System.out.println("You have been alive for " + days + " days.");

            if (hours >= 1000 && (hours % 1000) < 100) {
                int h = 0;
                System.out.println("You have slept for " + hours / 1000 + "," + h + hours % 1000 + " hours.");
            }

            else if (hours >= 1000)
                System.out.println("You have slept for " + hours / 1000 + "," + hours % 1000 + " hours.");

            else if (hours < 1)
                System.out.println("You have slept for 0 hours.");

            else
                System.out.println("You have slept for " + hours + " hours.");

        }

    }
}
