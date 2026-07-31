def dfs_n_queens(n):
    if n < 1:
        return []   
    solutions = []
    stack = [[]]
    while stack:
        current_board = stack.pop()
        current_row = len(current_board)
        if current_row == n:
            solutions.append(current_board)
            continue    
        for col in range(n - 1, -1, -1):
            is_safe = True
            for row, placed_col in enumerate(current_board):
                if placed_col == col:
                    is_safe = False
                    break
                if abs(placed_col - col) == abs(row - current_row):
                    is_safe = False
                    break     
            if is_safe:
                stack.append(current_board + [col])  
    return solutions
