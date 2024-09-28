def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n -2)

def main():
    n = 10  # Example input
    print(f"Fibonacci number at position {n} is {fibonacci(n)}")

if __name__ == "__main__":
    main()

# O(2^n) exponential time complexity. This is because each call to fibonacci(n) results in two additional recursive calls 
# to fibonacci(n-1) and fibonacci(n-2). The time complexity of this algorithm is determined by the number of 
# recursive calls that are made. Each recursive call processes one element, so the total number of recursive calls 
# is approximately 2^n. The running time of each recursive call is O(1), so the total running time is O(2^n).

# O(n) linear space complexity. since it uses recursion and the call stack grows with the size of the input. 
# Each recursive call requires additional memory to store the state of the function, and the total amount of 
# memory required increases linearly with the size of the input.