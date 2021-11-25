#3. Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12), яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь)

nm = int(input("Enter month number: "))

def season(nm):
  if nm == 1 or nm == 2 or nm == 12:
    print ("Winter")
  elif nm == 3 or nm == 4 or nm == 5:
    print ("Spring")
  elif nm == 6 or nm == 7 or nm == 8:
    print ("Summer")
  elif nm == 9 or nm == 10 or nm == 11:
    print ("Autmn")
  else:
    print ("Wrong input")
    
print (season(nm))
