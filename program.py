
hour_minute = []

for i in range(0,24):
    for j in range(0,60):
        if i <= 9:
            aux_hour = "0"+str(i)
        else:
            aux_hour = str(i)

        if j <= 9:
            aux_min = "0"+str(j)
        else:
            aux_min = str(j)

        hour_minute.append(aux_hour+aux_min)


print(hour_minute[3])

findin = ('1','3','5','7','9')
lista=[]

for value in hour_minute:
    lista.append([findin.count(item) for item in value])


numberImpar = 0

for x in lista:
    numberImpar+= sum(x)

print(numberImpar)