a= int(input("primeiro numero: "))
b= int(input("segundo numero: "))
c= int(input("terceito numero: "))

if (a <= b) and (a <= c):
    print 'menor numero: ', a
elif (b <= a) and (b <= c):
    print 'menorn numero: ', b
else:
    print 'menor numero: ', c
