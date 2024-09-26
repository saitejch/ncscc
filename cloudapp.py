def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Example usage
num_terms = 10  # Change this value to generate more or fewer terms
print(f"Fibonacci series up to {num_terms} terms: {fibonacci(num_terms)}")
