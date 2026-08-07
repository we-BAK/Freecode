import math

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

def calculate_rectangle_area(length, width):
    return length * width

def calculate_triangle_area(base, height):
    return 0.5 * base * height


print("=== 📐 Geometry Area Calculator ===")
print("1. Circle")
print("2. Rectangle / Square")
print("3. Triangle")

choice = input("\nSelect a shape (1-3): ")

if choice == "1":
    r = float(input("Enter radius: "))
    area = calculate_circle_area(r)
    print(f"👉 Area of Circle = {area:.2f}")

elif choice == "2":
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    area = calculate_rectangle_area(l, w)
    print(f"👉 Area of Rectangle = {area:.2f}")

elif choice == "3":
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    area = calculate_triangle_area(b, h)
    print(f"👉 Area of Triangle = {area:.2f}")

else:
    print("❌ Invalid choice! Please select 1, 2, or 3.")