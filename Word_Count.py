text = input("Enter a sentence: ")
words = text.split()

print(f"Total words: {len(words)}")
print(f"Reversed: {' '.join(reversed(words))}")