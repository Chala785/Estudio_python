""" -------- Variables --------  """


print("--- 1 ---")
my_string_variable = "My string variable"
print(my_string_variable)

print("--- 2 ---")
my_int_variable = 42
print(my_int_variable)

print("--- 3 ---")
my_bool_variable = False
print(my_bool_variable)

print("--- 4 ---")
print(my_string_variable, "-", my_int_variable, my_bool_variable)

print("--- 5 ---")
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

# Concatenación de variables en un print 
print("--- 6 ---")
print(my_string_variable, "-", my_int_to_str_variable, my_bool_variable)

print("--- 7 ---")
print("Este es el valor de:", my_bool_variable)

# Algunas de funciones del sistema (len) 
print("--- 8 ---")
print(len(my_string_variable)) # Cuanta la cantidad de caracteres 

# variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
print("--- 9 ---")
name, surname, alias, age = "Juan", "Gallego", "Chala", 20
print("Me llamo:" ,name, surname,"Mi alias es" , alias, "Mi edad es", age, "años")

# Inputs
# print("--- 10 ---")
# name = input('What is your name? ')
# age = input('What is your age? ')

# print(name)
# print(age)

# Cambiamos su tipo
print("--- 11 ---")
name = 20
age = "Juan"
print(name)
print(age)

# Forzamos el tipo de dato
print("--- 12 ---")
address: str = "Mi direccion"
address = True
print(type(address))





