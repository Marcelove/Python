a = int(input('Digite sua idade: \n'))
b = int(input('Agora, digite seus meses: \n'))
c = int (input('Diga quantos dias você tem: '))

dei = a*365
dem = b*30

dt = dei+dem+ c

print ('Seus dias totais de vida são: \n', dt)

#Exercício 3
x = int(input('Digite o tempo em segundos do exame: '))

y = x/60 #minute
z = y/60


print ('Seu tempo em segundos, minutos e horas foi: \n', x, '', y, '', z) #Ficou certo, porem tem como deixar mais bonito
