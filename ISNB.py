# 📚 ISBN VALIDATOR SYSTEM

def calculate_check_digit_10(digits):
    """Calculate ISBN-10 check digit."""

    total = sum(digit * (10 - index) for index, digit in enumerate(digits))

    result = 11 - (total % 11)

    if result == 11:
        return "0"
    elif result == 10:
        return "X"

    return str(result)


def calculate_check_digit_13(digits):
    """Calculate ISBN-13 check digit."""

    total = 0

    for index, digit in enumerate(digits):
        total += digit * (1 if index % 2 == 0 else 3)

    result = (10 - total % 10) % 10

    return str(result)


def validate_isbn(isbn, length):
    """Validate ISBN code."""

    # Check length
    if len(isbn) != length:
        return f"❌ ISBN-{length} must contain exactly {length} digits."

    # Separate main digits and check digit
    main_digits = isbn[:-1]
    given_check_digit = isbn[-1].upper()

    # Validate characters
    if not main_digits.isdigit():
        return "❌ Invalid characters found in ISBN."

    digits = [int(digit) for digit in main_digits]

    # Calculate expected check digit
    if length == 10:
        expected = calculate_check_digit_10(digits)
    else:
        expected = calculate_check_digit_13(digits)

    # Compare digits
    if given_check_digit == expected:
        return "✅ Valid ISBN Code!"

    return (
        f"❌ Invalid ISBN Code.\n"
        f"Expected check digit: {expected}\n"
        f"Received check digit: {given_check_digit}"
    )


def main():

    print("=" * 45)
    print("          📚 ISBN VALIDATOR")
    print("=" * 45)

    user_input = input(
        "Enter ISBN and length (example: 9783161484100,13): "
    )

    try:
        isbn, length = user_input.split(",")
        isbn = isbn.strip()
        length = int(length.strip())

    except ValueError:
        print("❌ Please enter values in format: ISBN,length")
        return


    if length not in (10, 13):
        print("❌ ISBN length must be 10 or 13.")
        return


    result = validate_isbn(isbn, length)

    print("-" * 45)
    print(result)
    print("=" * 45)


if __name__ == "__main__":
    main()