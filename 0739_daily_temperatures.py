# Traversing from the right techniques a general version of the sliding window techniques 
# for solving substring problems

# 739. Daily Temperatures

# Steps to solve:
# 1. initialize the temperature days interval with0 based on the len of temperature arrays
# 2. create a stack to store previous and next temperature
# 3. loop through the index and temperature and add the temp and the index
# 4. if value exist in the stack and the temperature is greater than the stack 
#  temperature pop the first value from the stack
# 5. set the wait_days value with the distance between the current index and the popped stack_index

def dailyTemperatures(temperatures):
    wait_days = [0] * len(temperatures)
    stack = [] #pair: [temp, index]

    for index, temp in enumerate(temperatures):
        while stack and temp > stack[-1][0]:
            _, stack_index = stack.pop()
            wait_days[stack_index] = (index - stack_index)
        stack.append([temp, index])
    return wait_days

temperatures = [73,74,75,71,69,72,76,73] #output: [1,1,4,2,1,1,0,0]
# temperatures = [30,40,50,60] #output: [1,1,1,0]
# temperatures = [30,60,90] #output: [1,1,0]
print(dailyTemperatures(temperatures))
