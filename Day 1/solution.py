# imports
import os
import itertools 

# function call files into into list
def retrieve_data(file):
  exists = os.path.isfile(file)
  if exists:
    with open(file, 'r') as infile:
      data = infile.read().splitlines() 
      expenses = list(map(int, data))
    return expenses
  else:
    raise SystemExit('File path passed to def retrieve_data(file) was not found.')

# function any two numbers in list that equal specific value
def check_expenses_2020_bytwo(nums, k):   
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == k:
                res = nums[i] * nums[j]
                return res
    return False

# function any three numbers in list that equal specific value
def check_expenses_2020_bythree(nums, l):   
    expenses = sorted(nums)
    for i in expenses:
        for j in expenses:
            if i + j > l:
                break
            for k in expenses:
                if i + j + k == l:
                    return i * j * k
                if i + j + k > l:
                    break

# Retrieve Dataset into list
data_set = retrieve_data("data.txt")

# Part 1
print(check_expenses_2020_bytwo(data_set, 2020))
# Part 2
print(check_expenses_2020_bythree(data_set, 2020))

