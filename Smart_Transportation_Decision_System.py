# 🚗 Smart Transportation Decision System

print("=" * 45)
print("     🚦 TRANSPORTATION DECISION SYSTEM")
print("=" * 45)

# 1. User Information
distance_mi = 3
is_raining = False
has_bike = True
has_car = False
has_ride_share_app = True

print(f"📍 Distance: {distance_mi} miles")
print(f"🌧️ Raining: {'Yes' if is_raining else 'No'}")
print(f"🚲 Has Bike: {'Yes' if has_bike else 'No'}")
print(f"🚗 Has Car: {'Yes' if has_car else 'No'}")
print(f"📱 Ride Share Available: {'Yes' if has_ride_share_app else 'No'}")

print("-" * 45)

# 2. Transportation decision logic
can_travel = False
transport_method = "None"

if distance_mi <= 0:
    print("❌ Invalid distance entered")

elif distance_mi <= 1:
    if not is_raining:
        can_travel = True
        transport_method = "🚶 Walking"
    else:
        transport_method = "☔ Wait for better weather"

elif distance_mi <= 6:
    if has_bike and not is_raining:
        can_travel = True
        transport_method = "🚲 Bicycle"
    else:
        transport_method = "🚫 Bike unavailable or bad weather"

else:
    if has_car:
        can_travel = True
        transport_method = "🚗 Personal Car"
    elif has_ride_share_app:
        can_travel = True
        transport_method = "📱 Ride Share"
    else:
        transport_method = "❌ No transportation available"

# 3. Final Result
print("=" * 45)
print("              RESULT")
print("=" * 45)

if can_travel:
    print("✅ Travel is possible!")
    print(f"🏆 Recommended method: {transport_method}")
else:
    print("❌ Travel is not possible")
    print(f"Reason: {transport_method}")

print("=" * 45)