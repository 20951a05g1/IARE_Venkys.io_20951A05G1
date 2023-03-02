//reverse a string using recursion in java

public class Reverse {
public static String reverse(String str) {
        if (str.isEmpty()) {
            return str;
        }
        else {
            return reverse(str.substring(1)) + str.charAt(0);
        }
    }
    public static void main(String[] args) {
        String str = "hello world";
        System.out.println(reverse(str));
    }
}
