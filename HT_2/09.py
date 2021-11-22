#9. Write a script to remove an empty tuple(s) from a list of tuples.
#Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
#Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

arr = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
arr2 = []
for e in arr:
    if len(e) != 0:
        arr2.append(e)
print(arr2)
