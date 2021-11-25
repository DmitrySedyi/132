# 6. Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> просто потицяв по клавi
#    Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
# -  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
# -  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
# -  якщо довжина бiльше 50 - > ваша фантазiя

s = input("Enter string: ")

def result(s):
  if len(s)	> 29 and len(s)	< 51:
    print ("Длинна строки: ")
    print (len(s))
    print ("Количество букв: ")
    print(len([i for i in s if i.isalpha()]))
    print ("Количкство цифр: ")
    print(len([i for i in s if i.isdigit()]))
  elif len(s)	< 30:
    print ("Cумма всех чисел: ")
    k=0
    for i in s:
        if i>="0" and i<="9":
          k += int(i)
    print(k)
    print ("Строка без цифр (только с буквами): ")
  elif len(s)	> 50:
    print("ваша фантазия")
    
    
print(result(s))  
