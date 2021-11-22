# Write a script to concatenate all elements in a list into a string and print it.

n = int(input("enter n: "))
l = list()

for i in range(n):
    S = str(input("enter something: "))
    l.append(S)
print("".join(l))

