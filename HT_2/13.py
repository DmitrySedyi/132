#13. Write a script to get the maximum and minimum value in a dictionary.

dict_1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

all_val = dict_1.values()
max_value = max(all_val)
min_value = min(all_val)

print("Maximum: ", max_value, "\nMinimum: ", min_value)
