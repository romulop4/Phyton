valor1= int(input("primeiro lado: "))
valor2= int(input("segundo lado: "))
valor3= int(input("terceito lado: "))

if (valor1 + valor2 < valor3) or (valor1 + valor3 < valor2) or (valor2 + valor3 < valor1):
    print'Nao e um triangulo'
elif (valor1 == valor2) or (valor2 == valor3) or (valor1 == valor3):
    altura = (((valor3/2)**2) + (valor1**2))**1/2
    area = (altura * valor1)/2
    print"a area do triangulo e: ", area
else:
    p = (valor1 + valor2 + valor3)/2
    area = (p*(p-valor1)*(p-valor2)*(p-valor3))**1/2
    print "a area do triangulo e: ", area


