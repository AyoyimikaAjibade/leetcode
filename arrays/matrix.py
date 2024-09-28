def create_matrix(n):
    matrix = []
    for _ in range(n):
        matrix.append([0] * n)
    return matrix

def main():
    n = 3  # Example size
    matrix = create_matrix(n)
    for row in matrix:
        print(row)

if __name__ == "__main__":
    main()

# O(n²) quadratic space complexity since the size of the matrix grows with the square of the size of the input (n). 
# The memory required to store the matrix increases proportionally to the size of the input.
