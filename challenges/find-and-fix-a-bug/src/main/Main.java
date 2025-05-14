public class Main {
    public static void main(String[] args) {
        ValidateISBN validator = new ValidateISBN();
        boolean result = validator.checkISBN("9781853260087");
        System.out.println("Is the ISBN valid? " + result);

        System.out.println(validator.checkISBN("0140449116")); // true (valid 10-digit ISBN)
        System.out.println(validator.checkISBN("9781853260087")); // true (valid 13-digit ISBN)
        System.out.println(validator.checkISBN("012000030X")); // true (valid 10-digit ISBN ending with 'X')
        System.out.println(validator.checkISBN("0140449117")); // false (invalid 10-digit ISBN)
        System.out.println(validator.checkISBN("9781853267336")); // false (invalid 13-digit ISBN)

    }
}