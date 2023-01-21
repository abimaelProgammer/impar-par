par = 0
Impar = 0
LPar = []
LImpar = []

num = int(input("Entre com um número ou 0 para parar: "))

while num != 0:
  if num % 2 == 0:
    par = par+1
    LPar.append(num)
  else:
    Impar = Impar + 1
    LImpar.append(num)
  num = int(input("Entre com um número ou 0 para parar: "))
print("Tem ",par," números pares")
print("Tem ", Impar, "Números impares")
print("Os números pares são: ",LPar)
print("Os números Impares são: ", LImpar)