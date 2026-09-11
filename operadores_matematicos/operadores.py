# aqui sabremos como se utiliza cada operador para sumar, restar, multiplicar, dividir etc...
# usare el mismo numero para todo que es 10 y 12 por que? por que sumas 10 + 12 es igual 22 y pues yo tengo 22 años xd
# comencemos disfruta y analiza cada ejemplo suerte :)

# suma
print(f"Suma: 10 + 12 = {10 + 12}")
# podemos hacerlo diferente manera igual
suma = 10 + 12
print(suma)

# resta
print(f"Resta: {10 - 12}")
resta = 10 - 12
print(resta)

# multiplicacion
print(f"Multiplicacion: {10 * 12}")
multiplicacion = 10 * 12
print(multiplicacion)

# division
print(f"Division: {10 / 12}")
division = 10 / 12
print(division)

# division entera
print(f"Division entera: {10 // 12}")
division_entera = 10 // 12
print(division_entera)

# modulo
print(f"Modulo: {10 % 12}")
modulo = 10 % 12
print(modulo)

# exponente
print(f"Exponente: {10 ** 12}")
exponente = 10 ** 12
print(exponente)

# seguimos aqui con los operadores para comparar los numeros

print(f"igualdad: 10 == 12 es {10 == 12}") # esto es False
print(f"desigualdad: 10 != 12 es {10 != 12}") # esto es True
print(f"mayor: 10 > 12 es {10 > 12}") # esto es False
print(f"menor: 10 < 12 es {10 < 12}") # esto es True
print(f"mayor igual que: 10 >= 12 es {10 >= 12}") # esto es False
print(f"menor igual que: 10 <= 12 es {10 <= 12}") # esto es True

# seguimos aqui con los operadores logicos para saber si es true o false

print(f"and: 10 + 12 == 22 and 12 - 10 == 2 es {10 + 12 == 22 and 12 - 10 == 2}") # esto es True
# podemos usar el or sin necesidad de usar el and igual daria true
print(f"or: 10 + 12 == 22 or 12 - 10 == 2 es {10 + 12 == 22 or 12 - 10 == 2}") # esto es True

# aqui van los false y true a la vez usariamos el not
print(f"not: 10 + 12 == 23 es {10 + 12 == 23}") # esto es False
# aqui mentimos en caso de que no se cumpla
print(f"not: not 10 + 12 == 23 es {not 10 + 12 == 23}") # esto es True

# seguimos con los operadores de asignacion de variables

my_variable = 12
print(my_variable)
my_variable += 12 # suma y asignacion
print(my_variable)
my_variable -= 12 # resta y asignacion
print(my_variable)
my_variable *= 12 # multiplicacion y asignacion
print(my_variable)
my_variable /= 12 # division y asignacion
print(my_variable)
my_variable //= 12 # division entera y asignacion
print(my_variable)
my_variable %= 12 # modulo y asinacion
print(my_variable)
my_variable **= 12 # exponente y asignacion
print(my_variable)

# seguimos con los operadores de identidad que esto es una direccion de memoria osea que cada una ocupa diferentes direcciones de memoria
# espero y me hayan entendido xd

my_nueva_variable = my_variable
print(f"my_variable is my_nueva_variable es {my_variable is my_nueva_variable}") # esto es True
print(f"my_variable is not my_nueva_variable es {my_variable is not my_nueva_variable}") # esto es False

# seguimos con los operadores de pertenencia en variables true or false 

print(f"'sa' in 'urilsa' = {'u' in 'urilsa'}") # esto es True
print(f"'py' not in 'urilsa' = {'py' not in 'urilsa'}") # esto es True
print(f"'ur' not in 'urilsa' = {'ur' not in 'urilsa'}") # esto es False

# seguimos con los operadores bit o (binarios)

sa = 10  # 1010
py = 12  # 1100

print(f"and: {sa} & {py} = {sa & py}")  # 1000
print(f"or: {sa} | {py} = {sa | py}")  # 1110
print(f"xor: {sa} ^ {py} = {sa ^ py}")  # 0110
print(f"not: ~{sa} = {~sa}") # 11110101
print(f"derecha: {sa} >> 2 = {sa >> 2}")  # 0010
print(f"izquierda: {sa} << 2 = {sa << 2}")  # 101000

# aqui tambien podemos usar numeros

#print(f"and: {10} & {12} = {10 & 12}")  # 1000
#print(f"or: {10} | {12} = {10 | 12}")  # 1110
#print(f"xor: {10} ^ {12} = {10 ^ 12}")  # 0110
#print(f"not: ~{10} = {~12}") # 11110101
#print(f"derecha: {10} >> 2 = {10 >> 2}")  # 0010
#print(f"izquierda: {10} << 2 = {10 << 2}")  # 101000

# espero que te haya servido estos ejemplos completos de operadores matematicos en el lenguaje de python
# no olvides seguirme y darle una estrellita ⭐ para seguir subiendo mas avances o ejemplos
# los quiero recuerden comer frutas y verduras y bañense xd
# 💙❤️
