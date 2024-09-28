def largestAltitude(gain):
    max_altitude = 0  # To store the maximum altitude encountered
    prev_diff = 0
    for i in range(len(gain)):
        alt_diff = prev_diff + gain[i] 
        max_altitude = max(alt_diff, max_altitude)
        prev_diff = alt_diff
    return max_altitude

# def largestAltitude(gain):
#         current_altitude = 0  # To store the current altitude during iteration
#         max_altitude = 0  # To store the maximum altitude encountered

#         # Iterate through the gain list, updating the current and max altitudes
#         for i in gain:
#             current_altitude += i
#             print('current_altitude', current_altitude, max_altitude)
#             max_altitude = max(current_altitude, max_altitude)

#         return max_altitude

def main():
#       arr = [-5, 1, 5, 0, -7]
#       arr = [4, -3, 2, -1, -2]
#       arr = [2, 2, -3, -1, 2, 1, -5]
      arr = [-838, -981, 750, 232, -960]
      result = largestAltitude(arr)
      print(result)

if __name__ == "__main__":
    main()

# time_complexity = O(n)
# space_complexity = O(1)