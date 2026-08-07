def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    if square_target == 0 or square_target == 1:
        print(f"The square root of {square_target} is {square_target}")
        return square_target
    low = 0.0
    high = max(1.0, float(square_target))
    for _ in range(max_iterations):
        mid = (low + high) / 2.0
        
        # Convergence condition strictly based on upper and lower bound difference
        if (high - low) <= tolerance:
            print(f"The square root of {square_target} is approximately {mid}")
            return mid
        
        if mid**2 < square_target:
            low = mid
        else:
            high = mid
            
    # 5. If maximum iterations reached without converging
    print(f"Failed to converge within {max_iterations} iterations")
    return None