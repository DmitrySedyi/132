#12. Write a script to concatenate following dictionaries to first one.
#Sample Dictionary :
#dic1={1:10, 2:20}
#dic2={3:30, 4:40}
#dic3={5:50,6:60}
#Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dict_1 = {1:10, 2:20}
dict_2 = {3:30, 4:40}			
dict_3 = {5:50, 6:60}
for d in (dict_2, dict_3): dict_1.update(d)
print (dict_1)
