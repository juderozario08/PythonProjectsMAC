def sum67(nums):
  result = 0
  counter = True
  for i in nums:
    if i == 6:
      counter = False
    elif not counter and i == 7:
      counter = True
    elif counter == True:
      result += i
  return result

print(sum67([2, 7, 6, 2, 6, 7, 2, 7]))