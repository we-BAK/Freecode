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


