# Grocery List Manager
grocery_list = []

def show_menu():
    print("\n=== 🛒 Grocery List Manager ===")
    print("1. View List")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Clear Entire List")
    print("5. Exit")

while True:
    show_menu()
    choice = input("\nChoose an option (1-5): ")

    if choice == "1":
        if not grocery_list:
            print("\n📋 Your grocery list is empty!")
        else:
            print("\n📋 Current Grocery List:")
            for index, item in enumerate(grocery_list, start=1):
                print(f"  {index}. {item}")

    elif choice == "2":
        new_item = input("\nEnter item to add: ").strip().capitalize()
        if new_item:
            grocery_list.append(new_item)
            print(f"✅ Added '{new_item}' to your list.")

    elif choice == "3":
        if not grocery_list:
            print("\n⚠️ List is empty. Nothing to remove.")
        else:
            item_to_remove = input("\nEnter item name or number to remove: ").strip()
            
            # Check if input is a item number or item name
            if item_to_remove.isdigit():
                idx = int(item_to_remove) - 1
                if 0 <= idx < len(grocery_list):
                    removed = grocery_list.pop(idx)
                    print(f"🗑️ Removed '{removed}'.")
                else:
                    print("❌ Invalid item number.")
            else:
                item_cap = item_to_remove.capitalize()
                if item_cap in grocery_list:
                    grocery_list.remove(item_cap)
                    print(f"🗑️ Removed '{item_cap}'.")
                else:
                    print(f"❌ '{item_to_remove}' is not in your list.")
    elif choice == "4":
        grocery_list.clear()
        print("\n🧹 Grocery list cleared!")
    elif choice == "5":
        print("\nGoodbye! Happy shopping! 🛍️")
        break
    else:
        print("\n❌ Invalid choice. Please enter a number between 1 and 5.")