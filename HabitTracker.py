import datetime
habits = {
    "Drink 2L Water": False,
    "Exercise for 20 mins": False,
    "Read 10 pages": False
}
print("=== 📅 Daily Habit Tracker ===")
print(f"Today's Date: {datetime.date.today()}\n")
while True:
    print("Your Habits for Today:")
    for index, (habit, done) in enumerate(habits.items(), start=1):
        status = "✅ Completed" if done else "❌ Pending"
        print(f"  {index}. {habit} [{status}]")
    print("\nOptions:")
    print("1. Mark a habit as complete")
    print("2. Add a new habit")
    print("3. Exit")
    choice = input("\nChoose an option (1-3): ")
    if choice == "1":
        num = int(input("Enter habit number to toggle: ")) - 1
        habit_keys = list(habits.keys())
        if 0 <= num < len(habit_keys):
            selected_habit = habit_keys[num]
            habits[selected_habit] = not habits[selected_habit]
            print(f"\nUpdated status for '{selected_habit}'!")
        else:
            print("\nInvalid habit number!")

    elif choice == "2":
        new_habit = input("Enter new habit name: ").strip().capitalize()
        if new_habit:
            habits[new_habit] = False
            print(f"\nAdded '{new_habit}' to your tracker!")

    elif choice == "3":
        print("\nKeep up the good work! Goodbye 👋")
        break

    else:
        print("\nInvalid choice. Try again!")
    print("-" * 30)