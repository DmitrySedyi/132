#8. Write a script to replace last value of tuples in a list.
#Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
#Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

n = input("enter last value of tuples in a list: ")
lstp = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

for e in lstp:
  arr = list(e)
  arr[-1] = n
  e = tuple(arr)
  print(e)
