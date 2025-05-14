// public class ValidateISBN {

// 	private static final int LONG_ISBN_MULTIPLIER = 10;
// 	private static final int SHORT_ISBN_MULTIPLIER = 11;
// 	private static final int SHORT_ISBN_LENGTH = 10;
// 	private static final int LONG_ISBN_LENGTH = 13;

// 	public boolean checkISBN(String isbn) {

// 		if (isbn.length() == LONG_ISBN_LENGTH) {
// 			return isThisAValidLongISBN(isbn);
// 		}
// 		else if (isbn.length() == SHORT_ISBN_LENGTH) {
// 			return isThisAValidShortISBN(isbn);			
// 		}
// 		throw new NumberFormatException("ISBN numbers must be 10 or 13 digits long");
// 	}

// 	private boolean isThisAValidShortISBN(String isbn) {
// 		int total = 0;

// 		for (int i = 0; i < SHORT_ISBN_LENGTH; i++)
// 		{
// 			if (!Character.isDigit(isbn.charAt(i))) {
// 				if (i ==9 && isbn.charAt(i) == 'X') {
// 					total += 10;
// 				}
// 				else {
// 					throw new NumberFormatException("ISBN numbers can only contain numeric digits");
// 				}
// 			}
// 			else {
// 				total += (isbn.charAt(i) - '0') * (SHORT_ISBN_LENGTH - i); // Fix: Subtract '0' to get numeric value
// 			}
// 		}

// 		return (total % SHORT_ISBN_MULTIPLIER == 0);
// 	}

// 	private boolean isThisAValidLongISBN(String isbn) {
// 		int total = 0;
		
// 		for (int i = 0; i < LONG_ISBN_LENGTH; i++) {
// 			if (i % 2 == 0) {
// 				total += (isbn.charAt(i) - '0'); // Fix: Subtract '0' to get numeric value
// 			} else {
// 				total += (isbn.charAt(i) - '0') * 3; // Fix: Subtract '0' to get numeric value
// 			}
// 		}
// 		return (total % LONG_ISBN_MULTIPLIER == 0);
// 	}
// }


import java.util.stream.IntStream;
import java.util.logging.Logger;

public class ValidateISBN {

    private static final int SHORT_ISBN_LENGTH = 10;
    private static final int LONG_ISBN_LENGTH = 13;
    private static final int SHORT_ISBN_MULTIPLIER = 11;
    private static final int LONG_ISBN_MULTIPLIER = 10;
	private static final Logger logger = Logger.getLogger(ValidateISBN.class.getName());

    public boolean checkISBN(String isbn) {

		try {
			if (isbn == null || isbn.isEmpty()) {
				throw new IllegalArgumentException("ISBN cannot be null or empty");
			}

			if (isbn.length() == SHORT_ISBN_LENGTH) {
				return validateISBN(isbn, SHORT_ISBN_LENGTH, SHORT_ISBN_MULTIPLIER, true);
			} else if (isbn.length() == LONG_ISBN_LENGTH) {
				return validateISBN(isbn, LONG_ISBN_LENGTH, LONG_ISBN_MULTIPLIER, false);
			} else {
				throw new NumberFormatException("ISBN must be either 10 or 13 digits long. Provided length: " + isbn.length());
			}
		}catch (NumberFormatException e) {
            logger.warning("Invalid ISBN: " + isbn + " - " + e.getMessage());
            throw e;
        }
    }

    private boolean validateISBN(String isbn, int length, int multiplier, boolean isShortISBN) {
        if (isShortISBN) {
            // Validate format for 10-digit ISBN (9 digits followed by a digit or 'X')
            if (!isbn.matches("^\\d{9}[\\dX]$")) {
                throw new NumberFormatException("Invalid 10-digit ISBN format: " + isbn);
            }
        } else {
            // Validate format for 13-digit ISBN (all digits)
            if (!isbn.matches("^\\d{13}$")) {
                throw new NumberFormatException("Invalid 13-digit ISBN format: " + isbn);
            }
        }

        int total = IntStream.range(0, length)
            .map(i -> {
                char currentChar = isbn.charAt(i);
                if (isShortISBN && i == 9 && currentChar == 'X') {
                    return 10; // Special case for 'X' in 10-digit ISBN
                } else {
                    int digit = currentChar - '0';
                    return isShortISBN ? digit * (length - i) : (i % 2 == 0 ? digit : digit * 3);
                }
            })
            .sum();

        return total % multiplier == 0;
	}
        

}