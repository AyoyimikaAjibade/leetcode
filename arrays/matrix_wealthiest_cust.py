def maximumWealth(accounts):
    max_wealth = 0  # Initialize max_wealth to 0
    for account in accounts:
        account_total_wealth = sum(account)
        # max_wealth = max(account_total_wealth, max_wealth)
        if account_total_wealth > max_wealth:
            max_wealth = account_total_wealth
    return max_wealth


def main():
    # arr = [[5,2,3],[0,6,7]]
    # arr = [[1,2],[3,4],[5,6]]
    arr = [[10,100],[200,20],[30,300]]
    result = maximumWealth(arr)
    print(result)

if __name__ == "__main__":
    main()

# time_complexity = O(n * m)
# n represent number of customers
# m represent number of accounts
# space_complexity = O(1)