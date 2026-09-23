#Operadores Python
#Operador de aritmética
print(2+2)
print(2*3) #Multiplicación
print(2-3) #Resta
print(10%3) #Módulo
print(10/3) #División
print(10//3) #División entera
print(10**3) #Potencia

#Operadores de comparación
print(2==2) #Igualdad
print(2<3) #Menor que
print(2>3) #Mayor que
print(2<=3) #Menor o igual que
print(2>=3) #Mayor o igual que
print(2!=3) #Diferente que

Copas_Mundo_de_Messi =1
Copas_Mundo_de_Cristiano =0

MESSI = Copas_Mundo_de_Messi 
CRISTIANO = Copas_Mundo_de_Cristiano
print(MESSI is CRISTIANO) #False
print(MESSI > CRISTIANO) #True

#Operadores lógicos
print(True and False) #dos cosas se tienen que cumplir
print(True or False) #una de las dos cosas se tiene que cumplir
print(not True) #lo contrario de lo que se cumple

#Operadores de asignacion
a = 5
print(a) #5
a += 3 #a = a + 3
print(a) #8
a -= 3 #a = a - 3
print(a) #5
a *= 3 #a = a * 3
print(a) #15
a /= 3 #a = a / 3
print(a) #5.0
a %= 3 #a = a % 3
print(a) #2.0

#Operadores de identidad

Messi = "Zurdo"
Cristiano = "Diestro"
print(Messi is "Zurdo") #True
print(Cristiano is not "Zurdo") #True

#Operadores de pertenencia

Messi = "1_Copa_del_Mundo"
print("1_Copa" in Messi) #True
Cristiano = "0_Copas_del_Mundo"
print("1_Copa_del_Mundo" not in Cristiano) #True

#Operadores de bits

print(2<<5) #Desplazamiento a la derecha
print(2>>5) #Desplazamiento a la izquierda

print(2 & 3) #AND
print(2 | 3) #OR
print(2 ^ 3) #XOR


for i in range(10, 56):
    if i % 2 == 0:
        if i % 3 != 0:
            if not i == 16:
                print(i)

#Otra manera de escribirlo

for i in range(10, 56):
    if i % 2 == 0 and i % 3 != 0 and not i == 16:
        print(i)


#Condicionales

nota = 8

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")

Stamina = 100
while Stamina > 0:
    print("Stamina: ", Stamina)
    Stamina -= 10

for i in range(10):
    if i == 5:
        break        # sale del bucle entero
    print(i)

for i in range(10):
    if i % 2 != 0:
        continue     # salta a la siguiente vuelta
    print(i)


#Piedra papel y tijeras

i= Jugador1
j= Jugador2

a= "Piedra"
b= "Tijeras"
c= "Papel"

if i == "Piedra" and j == "Tijeras":
    print("Gana Jugador 1")
elif i == "Tijeras" and j == "Papel":
    print("Gana Jugador 1")
elif i == "Papel" and j == "Piedra":
    print("Gana Jugador 1")
elif i == j:
    print("Empate")
else:
    print("Gana Jugador 2")
