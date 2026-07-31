def knapsack_2d(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            exclude_item = dp[i - 1][w]
            
            if weights[i - 1] <= w:
                include_item = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                dp[i][w] = max(exclude_item, include_item)
            else:
                dp[i][w] = exclude_item
                
    return dp[n][capacity]

item_values = [60, 100, 120]
item_weights = [10, 20, 30]
knapsack_capacity = 50

max_profit = knapsack_2d(item_weights, item_values, knapsack_capacity)
print(f"Maximum value in Knapsack = {max_profit}")  # Expected Output: 220
