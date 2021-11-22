#11. Write a script to remove duplicates from Dictionary.

d = {1: 10, 2: 20, 3: 30, 4: 30, 5: 50, 6: 60}
d2 = {}

for uv in d.values():
  for key, val in d.items():
    if uv == val:
      d2[key] = val
      break
print (d2)
