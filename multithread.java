import java.util.Scanner;

public class StringReverseMultiThread {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a string to reverse: ");
        String str = scanner.nextLine();

        Thread thread = new Thread(() -> {
            String reversed = reverse(str);
            System.out.println("Reversed string: " + reversed);
        });
        thread.start();
    }

    public static String reverse(String str) {
        if (str.isEmpty()) {
            return str;
        }
        return reverse(str.substring(1)) + str.charAt(0);
    }

}
