def diagonalSum(mat):
    n = len(mat)
    total_sum = 0  # Initialize the total sum
    for i in range(n):
        total_sum += mat[i][i] + mat[i][n-i-1] #3-0-1, 3-1-1, 3-2-1
    if n % 2 != 0:
        total_sum -= mat[n//2][n//2] # mat[1][1]
    return total_sum  # Return the calculated total sum

def main():
    arr = [
        [1,2,3],
        [4,5,6],
        [7,8,9]]
    # arr = [
    #     [1,0],
    #     [0,1]]
    # arr = [[5]]
    result = diagonalSum(arr)
    print(result)

if __name__ == "__main__":
    main()

# time_complexity = O(n)
# space_complexity = O(1)