import java.util.Scanner;

public class TimeConversion {
    public static void main(String[] args) {

        try (Scanner scan = new Scanner(System.in)) {
            System.out.println("Enter the time in minutes: ");
            int minutes = scan.nextInt();

            int hours = minutes / 60;
            int m = minutes % 60;

            if (m < 10)
                System.out.println("The time is " + hours + ":0" + m);

            else
                System.out.println("The time is " + hours + ":" + m);

        }

    }
}