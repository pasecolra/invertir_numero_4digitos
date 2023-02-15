# invertir un numero de 4 digitos

# input

A = int(input("se ingresa un numero de 4 digitos: "))

# processing

<<<<<<< HEAD
c4 = (A%10) * 1000
pe = A//10
c3 = (pe%10) * 100
pe = pe//10
c2 = (pe%10) * 10
c1 = pe // 10

nj = c4 + c3 + c2 + c1
=======
c4 = A % 10
c3 = int((A % 100) / 10)
c2 = int((A % 1000) / 100) 
c1 = int((A - (A % 1000)) / 1000)
>>>>>>> 2cf1cf9e3cd2fc0789b72f26fb98fd66988fee88

# output

print("----------------------------------------")
print("----------------RESULTADO---------------")
print("----------------------------------------")
 
<<<<<<< HEAD

print("NUMERO INVERSO: " + str(nj))
=======
print(" NUMERO INNVERSO: " + str(c4) + str(c3) + str(c2) + str(c1))

>>>>>>> 2cf1cf9e3cd2fc0789b72f26fb98fd66988fee88
