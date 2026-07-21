# 🍽️ Interactive Bill Splitter

print("=" * 40)
print("        🍴 BILL SPLITTER 🍴")
print("=" * 40)

num_of_friends = int(input("👥 Enter the number of friends: "))

appetizers = float(input("🥗 Enter the cost of appetizers: $"))
main_courses = float(input("🍝 Enter the cost of the main courses: $"))
desserts = float(input("🍰 Enter the cost of desserts: $"))
drinks = float(input("🥤 Enter the cost of drinks: $"))

subtotal = appetizers + main_courses + desserts + drinks
tip = subtotal * 0.25
total = subtotal + tip
per_person = total / num_of_friends

# Display receipt
print("\n" + "=" * 40)
print("            🧾 RECEIPT")
print("=" * 40)
print(f"🥗 Appetizers : ${appetizers:.2f}")
print(f"🍝 Main Course: ${main_courses:.2f}")
print(f"🍰 Desserts   : ${desserts:.2f}")
print(f"🥤 Drinks     : ${drinks:.2f}")
print("-" * 40)
print(f"💰 Subtotal   : ${subtotal:.2f}")
print(f"🎁 Tip (25%)  : ${tip:.2f}")
print(f"🧾 Total Bill : ${total:.2f}")
print("=" * 40)
print(f"👥 Friends    : {num_of_friends}")
print(f"💵 Each Pays  : ${per_person:.2f}")
print("=" * 40)
print("🎉 Enjoy your meal!")