# Question1
# Something related to IPO offering
# main gist is we had shares - lets say N which we want to divide among bidders
# Bidders are represented in 2d arrays as
# [bidder_id, no of shares_bid, price, timestamp]
# Now build a function returns the bidder_id's in sorted array that did not receive any shares.


# Shares are allocated following rules-

# 1. if the price is highest among all the bidders. Allocate shares
# 2. If the price is same among 2 bidders. Allocate share in iterative fashion, first one get share had earlier timestamp.
# Like 2 bidders with bidder id 1&2, have same price, timestamp 4 and 1, bids for 5 shares each and N=1.
# So, in this case only bidder id 1 get share, bidder id 2 will not recieve any shares
# Solution Approch


# Sort arrary by bidder price(descending) and timestamp(ascending)
# Iterate through array,
# if price[i] == price[i+1]:


# make tempory array to store id
# add no of shrare bids = temp_share_allocated
# else:


# see if temp_share_allocated has value > 0 -- handle it
# otherwise subtract from N
# Iterate over rest of array to find bidders that did not receive any shares.
# Sort the array of bidders with no shares and return that array
# Please take care of edge case - I was only able to solve 9/15


# Question 2
# https://leetcode.com/problems/consecutive-numbers-sum/
# Modification is numbers are positive and have to be consecutive. Not a single number.
# For num=250. output should be 3.
# For num=21. output should be 3.