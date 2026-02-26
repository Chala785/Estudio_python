""" ------ arithmetic operators ------- """

print(2 + 5) # suma
print(2 - 5) # resta
print(2 * 5) # multiplicación
print(2 / 5) # división
print(10 % 5) # módulo o resto de la división
print(10 // 5) # división entera o floor division
print(2 ** 5) # potencia
print(2 ** 3 + 3 - 7 / 1 //4) 

print("Hola" + "Python" + "¿Que tal?") # concatenación de strings
# no se puede restar ni multiplicar strings, da error
# print("Hola" + 5) # error, no se pueden sumar un string y un int
print("Hola " + str(5)) # se puede convertir el int a string para concatenar
print("Hola " * 5) # se puede multiplicar un string por un int para repetirlo
print("Hola " * (2 ** 3)) 


my_float = 2.5 * 2
print("Hola " * int(my_float)) 

""" ------ comparative operators ------- """

# Int
print("----- int -----")
print(3 > 4) # mayor que
print(3 < 4) # menor que
print(3 >= 4) # mayor o igual que
print(3 <= 4) # menor o igual que
print(3 == 4) # igual que
print(3 != 4) # diferente de

# String
print("----- string -----")
print("Hola" > "Python") 
print("Hola" < "Python")  
print("aaaa" >= "abaa") # Ordenaciòn alfabética por ASCII
print(len("aaaa") >= len("abaa")) # Cuenta caracteres
print("Hola" <= "Python") 
print("Hola" == "Python") 
print("Hola" != "Python")

""" ------ logical operators ------- """

print("----- Int with string -----")
print(3 > 4 and "Hola" > "Python") 
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python") 
print(3 < 4 or "Hola" > "Python")
print(not(3 > 4))