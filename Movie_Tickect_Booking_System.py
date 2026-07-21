# 🎬 Movie Ticket Booking System

print("=" * 45)
print("        🎥 MOVIE TICKET BOOKING 🎥")
print("=" * 45)

# Ticket information
base_price = 15
age = 21
seat_type = 'Gold'
show_time = 'Evening'

# Membership information
is_member = False
is_weekend = False

# Check age eligibility
if age > 17:
    print("✅ User is eligible to book a ticket")

if age >= 21:
    print("🌙 User is eligible for Evening shows")
else:
    print("❌ User is not eligible for Evening shows")

print("-" * 45)

# Membership discount
discount = 0

if is_member and age >= 21:
    discount = 3
    print("🎟️ Membership discount applied")
else:
    print("ℹ️ No membership discount available")

print(f"💸 Discount: ${discount:.2f}")

print("-" * 45)

# Weekend / Evening extra charges
extra_charges = 0

if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print("🌙 Evening/weekend extra charge applied")
else:
    print("✅ No extra charges applied")

print(f"➕ Extra charges: ${extra_charges:.2f}")

print("-" * 45)

# Ticket booking condition
if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):

    print("🎉 Ticket booking condition satisfied")

    # Seat service charges
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1

    print(f"💺 Seat Type: {seat_type}")
    print(f"🛠️ Service charges: ${service_charges:.2f}")

    # Final price calculation
    final_price = base_price + extra_charges + service_charges - discount

    print("=" * 45)
    print("             🧾 FINAL RECEIPT")
    print("=" * 45)
    print(f"🎬 Show Time       : {show_time}")
    print(f"💺 Seat Type       : {seat_type}")
    print(f"🎫 Base Price      : ${base_price:.2f}")
    print(f"➕ Extra Charges   : ${extra_charges:.2f}")
    print(f"🛠️ Service Charges : ${service_charges:.2f}")
    print(f"🎟️ Discount        : -${discount:.2f}")
    print("-" * 45)
    print(f"💰 Final Ticket Price: ${final_price:.2f}")
    print("=" * 45)
    print("🍿 Enjoy your movie!")

else:
    print("❌ Ticket booking failed due to restrictions")