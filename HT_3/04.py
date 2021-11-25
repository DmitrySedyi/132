#4. Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат. 
#Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi, обробляє повернутий ними результат та також повертає результат. 
#Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3

a = int(input("Enter 1 number :"))
b = int(input("Enter 2 number :"))
c = int(input("Enter 3 number :"))


def sum(a,b,c):
  return a+b+c
  
def ymnoj(a,b,c): 
  return a*b*c
  
def minus(a,b,c):
  return a-b-c

  
def story():
  print ("Сумма: ")
  print(sum(a,b,c))
  print ("Произведение: ")
  print(ymnoj(a,b,c))
  print ("Частное: ")
  print(minus(a,b,c))

print (story())
