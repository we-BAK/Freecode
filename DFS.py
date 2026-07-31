def dfs(matrix, start_node):
    visited = []
    stack = [start_node] 
    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            visited.append(current_node)
            for neighbor in range(len(matrix[current_node])):
                if matrix[current_node][neighbor] == 1 and neighbor not in visited:
                    stack.append(neighbor)
                    
    return visited
