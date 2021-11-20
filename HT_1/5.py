decimal = int(input("Enter the decimal value: "))

porovny = decimal // 16
ostatok = decimal % 16

if ostatok == 10:
    print ("hexadecimal: " + str(porovny) + "A")
elif ostatok == 11:
    print ("hexadecimal: " + str(porovny) + "B")
elif ostatok == 12:
    print ("hexadecimal: " + str(porovny) + "C")
elif ostatok == 13:
    print ("hexadecimal: " + str(porovny) + "D")
elif ostatok == 14:
    print ("hexadecimal: " + str(porovny) + "E")
elif ostatok == 15:
    print ("hexadecimal: " + str(porovny) + "F") 
elif ostatok == 0:
    print ("hexadecimal: " + str(porovny)) 
else:
    print ("hexadecimal: " + str(porovny) + str(ostatok))
