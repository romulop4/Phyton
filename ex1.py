
dataRecebida= int(input("Sua idade em dias: "))
dataAno = dataRecebida/365
dataRecebida = dataRecebida - (dataAno*365)
dataMeses = dataRecebida/30
dataRecebida = dataRecebida - (dataMeses*30)
dataDias = dataRecebida

print("Sua idade e: ", dataAno," anos", dataMeses," meses", dataDias," dias")