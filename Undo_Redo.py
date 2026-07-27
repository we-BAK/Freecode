class Node:
    def __init__(self, state: str):
        self.state = state  
        self.prev = None    
        self.next = None    


class TextEditor:
    def __init__(self, initial_text: str = ""):
        self.current = Node(initial_text)

    def write(self, new_text: str):
        """Appends text and creates a new state in history."""
        updated_text = self.current.state + new_text
        new_node = Node(updated_text)

        self.current.next = new_node
        new_node.prev = self.current

       
        self.current = new_node

    def undo(self) -> str:
        """Goes back to the previous state if available."""
        if self.current.prev:
            self.current = self.current.prev
        return self.current.state

    def redo(self) -> str:
        """Moves forward to the next state if available."""
        if self.current.next:
            self.current = self.current.next
        return self.current.state

    def get_text(self) -> str:
        """Returns the current document text."""
        return self.current.state


# --- Demo Usage ---
if __name__ == "__main__":
    editor = TextEditor()

    editor.write("Hello")
    editor.write(" World")
    editor.write("!")
    print("Current Text:", editor.get_text())  # Output: Hello World!

    print("\n--- Undo Twice ---")
    print("Undo 1:", editor.undo())  # Output: Hello World
    print("Undo 2:", editor.undo())  # Output: Hello

    print("\n--- Redo Once ---")
    print("Redo 1:", editor.redo())  # Output: Hello World

    print("\n--- Write New Text ---")
    editor.write(" Everyone")
    print("Current Text:", editor.get_text())  # Output: Hello World Everyone

    print("Redo attempt:", editor.redo())  # Output: Hello World Everyone