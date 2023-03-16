#Find the highest number in a list of random numbers 

#1st eaxample
numbers = [5, 2, 5, 9, 6, 12, 14, 7]
numbers.sort()
print(numbers[-1])

#2nd example
new_numbers = [3,7,4,6,3,2,9,5,12,11]
max_num = 0
for num in new_numbers:
  if max_num > num:
    continue
  else:
    max_num = num
print(max_num)