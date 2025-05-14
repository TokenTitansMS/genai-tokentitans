// import static org.junit.jupiter.api.Assertions.*;

// import org.junit.jupiter.api.Test;

// class ValidateISBNTest {

// 	@Test
// 	public void checkAValid10DigitISBN() {
// 		ValidateISBN validator = new ValidateISBN();
// 		boolean result = validator.checkISBN("0140449116");
// 		assertTrue(result,"first value");
// 		result = validator.checkISBN("0140177396");
// 		assertTrue(result, "second value");
// 	}
	
// 	@Test
// 	public void checkAValid13DigitISBN() {
// 		ValidateISBN validator = new ValidateISBN();
// 		boolean result = validator.checkISBN("9781853260087");
// 		assertTrue(result,"first value");
// 		result = validator.checkISBN("9781853267338");
// 		assertTrue(result, "second value");
// 	}
	
// 	@Test
// 	public void TenDigitISBNNumbersEndingInAnXAreValid() {
// 		ValidateISBN validator = new ValidateISBN();
// 		boolean result = validator.checkISBN("012000030X");
// 		assertTrue(result);
// 	}

// 	@Test
// 	public void checkAnInvalid10DigitISBN() {
// 		ValidateISBN validator = new ValidateISBN();
// 		boolean result = validator.checkISBN("0140449117");
// 		assertFalse(result);
// 	}
	
// 	@Test
// 	public void checkAnInvalid13DigitISBN() {
// 		ValidateISBN validator = new ValidateISBN();
// 		boolean result = validator.checkISBN("9781853267336");
// 		assertFalse(result);
// 	}
	
// 	@Test
// 	public void nineDigitISBNsAreNotAllowed() {
// 		ValidateISBN validator = new ValidateISBN();
// 		assertThrows(NumberFormatException.class, 
// 				() -> {
// 					validator.checkISBN("123456789");
// 				});
// 	}
	
// 	@Test
// 	public void nonNumericISBNsAreNotAllowed() {
// 		ValidateISBN validator = new ValidateISBN();
// 		assertThrows(NumberFormatException.class, 
// 				() -> {
// 					validator.checkISBN("helloworld");
// 				});
// 	}
	
	
// }


import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class ValidateISBNTest {

    @Test
    public void checkAValid10DigitISBN() {
        ValidateISBN validator = new ValidateISBN();
        assertTrue(validator.checkISBN("0140449116"), "Valid 10-digit ISBN");
        assertTrue(validator.checkISBN("0140177396"), "Valid 10-digit ISBN");
    }

    @Test
    public void checkAValid13DigitISBN() {
        ValidateISBN validator = new ValidateISBN();
        assertTrue(validator.checkISBN("9781853260087"), "Valid 13-digit ISBN");
        assertTrue(validator.checkISBN("9781853267338"), "Valid 13-digit ISBN");
    }

    @Test
    public void check10DigitISBNEndingInX() {
        ValidateISBN validator = new ValidateISBN();
        assertTrue(validator.checkISBN("012000030X"), "Valid 10-digit ISBN ending with 'X'");
    }

    @Test
    public void checkAnInvalid10DigitISBN() {
        ValidateISBN validator = new ValidateISBN();
        assertFalse(validator.checkISBN("0140449117"), "Invalid 10-digit ISBN");
    }

    @Test
    public void checkAnInvalid13DigitISBN() {
        ValidateISBN validator = new ValidateISBN();
        assertFalse(validator.checkISBN("9781853267336"), "Invalid 13-digit ISBN");
    }

    @Test
    public void checkInvalidLengthISBN() {
        ValidateISBN validator = new ValidateISBN();
        assertThrows(NumberFormatException.class, 
            () -> validator.checkISBN("123456789"), 
            "9-digit ISBNs are not allowed");
        assertThrows(NumberFormatException.class, 
            () -> validator.checkISBN("12345678901234"), 
            "14-digit ISBNs are not allowed");
    }

    @Test
    public void checkNonNumericISBN() {
        ValidateISBN validator = new ValidateISBN();
        assertThrows(NumberFormatException.class, 
            () -> validator.checkISBN("helloworld"), 
            "Non-numeric ISBNs are not allowed");
        assertThrows(NumberFormatException.class, 
            () -> validator.checkISBN("97818532X7336"), 
            "ISBNs with invalid characters are not allowed");
    }

    @Test
    public void checkNullOrEmptyISBN() {
        ValidateISBN validator = new ValidateISBN();
        assertThrows(IllegalArgumentException.class, 
            () -> validator.checkISBN(null), 
            "Null ISBNs are not allowed");
        assertThrows(IllegalArgumentException.class, 
            () -> validator.checkISBN(""), 
            "Empty ISBNs are not allowed");
    }

    @Test
    public void checkEdgeCases() {
        ValidateISBN validator = new ValidateISBN();
        assertTrue(validator.checkISBN("0000000000"), "Valid 10-digit ISBN with all zeros");
        assertTrue(validator.checkISBN("9780000000002"), "Valid 13-digit ISBN with all zeros except checksum");
        assertFalse(validator.checkISBN("0000000001"), "Invalid 10-digit ISBN with all zeros except last digit");
        assertFalse(validator.checkISBN("9780000000000"), "Invalid 13-digit ISBN with all zeros");
    }

    @Test
    public void checkISBNWithSpacesOrSpecialCharacters() {
        ValidateISBN validator = new ValidateISBN();
        assertThrows(NumberFormatException.class, 
            () -> validator.checkISBN("978 1853260087"), 
            "ISBNs with spaces are not allowed");
        assertThrows(NumberFormatException.class, 
            () -> validator.checkISBN("978-1853260087"), 
            "ISBNs with dashes are not allowed");
    }

    @Test
    public void checkISBNWithLeadingOrTrailingWhitespace() {
        ValidateISBN validator = new ValidateISBN();
        assertThrows(NumberFormatException.class, 
            () -> validator.checkISBN(" 9781853260087"), 
            "ISBNs with leading whitespace are not allowed");
        assertThrows(NumberFormatException.class, 
            () -> validator.checkISBN("9781853260087 "), 
            "ISBNs with trailing whitespace are not allowed");
    }

    @Test
    public void checkISBNWithInvalidCharactersIn10DigitISBN() {
        ValidateISBN validator = new ValidateISBN();
        assertThrows(NumberFormatException.class, 
            () -> validator.checkISBN("01234567A9"), 
            "10-digit ISBNs with invalid characters are not allowed");
    }

    @Test
    public void checkISBNWithInvalidCharactersIn13DigitISBN() {
        ValidateISBN validator = new ValidateISBN();
        assertThrows(NumberFormatException.class, 
            () -> validator.checkISBN("97818532600A7"), 
            "13-digit ISBNs with invalid characters are not allowed");
    }
}