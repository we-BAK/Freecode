def meters_to_feet(meters):
    return meters * 3.28084

def kg_to_lbs(kg):
    return kg * 2.20462

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


print("=== 🔄 Simple Unit Converter ===")
print("1. Meters to Feet")
print("2. Kilograms to Pounds")
print("3. Celsius to Fahrenheit")

choice = input("\nSelect a conversion (1-3): ")

if choice == "1":
    meters = float(input("Enter distance in meters: "))
    print(f"👉 {meters} meters = {meters_to_feet(meters):.2f} feet")

elif choice == "2":
    kg = float(input("Enter weight in kilograms: "))
    print(f"👉 {kg} kg = {kg_to_lbs(kg):.2f} lbs")

elif choice == "3":
    c = float(input("Enter temperature in Celsius: "))
    print(f"👉 {c}°C = {celsius_to_fahrenheit(c):.2f}°F")

else:
    print("❌ Invalid choice! Please enter 1, 2, or 3.")