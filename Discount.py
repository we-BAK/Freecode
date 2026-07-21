def apply_discount(price: float, discount: float):
    """
    Calculate the final price after applying a percentage discount.

    Args:
        price (float): Original product price.
        discount (float): Discount percentage (0-100).

    Returns:
        float | str: Final price or an error message.
    """

    # Validate price type
    if isinstance(price, bool) or not isinstance(price, (int, float)):
        return "❌ The price should be a number"

    # Validate discount type
    if isinstance(discount, bool) or not isinstance(discount, (int, float)):
        return "❌ The discount should be a number"

    # Validate price value
    if price <= 0:
        return "❌ The price should be greater than 0"

    # Validate discount range
    if not 0 <= discount <= 100:
        return "❌ The discount should be between 0 and 100"

    # Calculate discount
    discount_amount = price * (discount / 100)
    final_price = price - discount_amount

    return final_price


# 🛒 Example Usage
product_price = 250
discount_percentage = 20

result = apply_discount(product_price, discount_percentage)

print("=" * 40)
print("          🛍️ DISCOUNT RECEIPT")
print("=" * 40)

if isinstance(result, str):
    print(result)
else:
    print(f"Original Price : ${product_price:.2f}")
    print(f"Discount       : {discount_percentage}%")
    print(f"Saved Amount   : ${product_price - result:.2f}")
    print(f"Final Price    : ${result:.2f}")

print("=" * 40)
print("✨ Thank you for shopping!")