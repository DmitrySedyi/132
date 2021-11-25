# 7. Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!

x = int(input("Enter x: "))
y = int(input("Enter y: "))
op = input("Enter znak (+,-,*,/): ")


def result(x,y,op):
  if op == "+":
    return x+y
  elif op == "-":
    return x-y
  elif op == "*":
    return x*y
  elif op == "/":
    return x/y
    
print(result(x,y,op))   


more = input("More (y/n) : ")

while more == "y":
  if more == "y":
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    op = input("Enter znak (+,-,*,/): ")
    print(result(x,y,op))   
    more = input("More (y/n) : ")
else:
    print("Have a great day!")
