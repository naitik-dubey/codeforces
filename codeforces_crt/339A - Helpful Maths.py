'''
In this problem we have given a string which contain 4 character '1','2','3','+':
and we need to sort the number in the ascending order and '+' sign will be in between all the number

first take the input
second split the '+' sign form the string
third convert the remaining number into the int
fourth sort the numbers
fifth convert the list into the string and add the '+' sign in between the numbers. with the help of join.
'''

s = input().strip()           # Read the string
nums = s.split('+')           # Split into list: e.g., ['3', '2', '1']
nums.sort()                   # Sort the list: ['1', '2', '3']
result = '+'.join(nums)       # Join back into string: '1+2+3'
print(result)