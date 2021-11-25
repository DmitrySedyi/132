#2. Користувачем вводиться початковий і кінцевий рік. Створити цикл, який виведе всі високосні роки в цьому проміжку (границі включно).

sy = int(input("Enter start year: "))
ey = int(input("Enter end year: "))

if sy >= ey:
 print("Check your year input again.")
 
if sy < ey:
  print ("Here is a list of leap years between " + str(sy) + " and " + str(ey)  + ":")
print (sy)  
while sy <= ey:
  if sy % 4 == 0 and sy % 100 != 0:
    print(sy)
  if sy % 100 == 0 and sy % 400 == 0:
    print(sy)
  sy += 1
