import bisect

class DatabaseIndex:
    def __init__(self):
        self.keys = []    # Sorted list of record IDs
        self.values = []  # Corresponding record payloads

    def insert(self, key: int, value: str):
        # Find index to keep array sorted (Binary Search)
        idx = bisect.bisect_left(self.keys, key)
        self.keys.insert(idx, key)
        self.values.insert(idx, value)

    def find(self, key: int):
        # Locate exact position in O(log N) using Binary Search
        idx = bisect.bisect_left(self.keys, key)
        if idx < len(self.keys) and self.keys[idx] == key:
            return self.values[idx]
        return "Record Not Found"

# Demo
db = DatabaseIndex()
for i in range(0, 1000000, 2):  # Populate 500k records (even numbers)
    db.insert(i, f"User_Data_{i}")

print(db.find(49202))  # Output: User_Data_49202 (Instant lookup!)