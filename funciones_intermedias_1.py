#1) Actualizar valores en diccionarios y listas
print("----------EJERCICIO 1----------")
matriz = [ [10, 15, 20], [3, 7, 14] ]

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
] 

ciudades = {
    "México": ["Ciudad de Mexico", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
} 

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

# A) Cambia el valor de 3 en matriz por 6. 
matriz [1] [0] = 6
print (matriz)

# B) Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”  

cantantes [0] ["nombre"]= "Enrique Martin Morales"
print(cantantes)
# C) En ciudades, cambia “Cancún” por “Monterrey”

ciudades  ["México"] [2] = "Monterrey"
print (ciudades)

# D) En las coordenadas, cambia el valor de “latitud” por 9.9355431

coordenadas [0] ["latitud"] = 9.9355431
print (coordenadas)

#2) Iterar a través de una lista de diccionarios
print("----------EJERCICIO 2----------")
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]
# Crea la función iterarDiccionario(lista) que reciba una lista de diccionarios y 
#recorra cada diccionario de la lista e imprima cada llave y el valor correspondiente. 

def iterarDiccionario(lista):
    for diccionario in lista:
        print(", ".join(f"{k} - {v}" for k, v in diccionario.items()))

iterarDiccionario(cantantes)


#3. Obtener valores de una lista de diccionarios

#A)Crea la función iterarDiccionario2(llave, lista) que reciba una cadena con el nombre de una llave 
# y una lista de diccionarios.
#  La función debe imprimir el valor almacenado para esa clave de cada diccionario que se encuentra
#  en la lista.
#Debe imprimir:
#-Ricky Martin
#-Chayanne
#-José José
#-Juan Luis Guerra
print("----------EJERCICIO 3----------")
def iterarDiccionario2(llave,lista):
    for dic1 in lista:
        print(dic1[llave])

iterarDiccionario2("nombre", cantantes)

#B) Otro ejemplo: iterarDiccionario2(“pais”, cantantes) debe de imprimir:

#Puerto Rico
#Puerto Rico
#México
#República Dominicana

def iterarDiccionario2(llave,lista):
    for dic2 in lista:
        print(dic2[llave])

iterarDiccionario2("pais", cantantes)

#4. Iterar a través de un diccionario con valores de lista

#Crea una función imprimirInformacion(diccionario) 
# que reciba un diccionario en donde los valores son listas.
#  La función debe imprimir el nombre de cada clave junto con el tamaño de su lista
#  y seguido de esto los valores de la lista para esa clave.
print("----------EJERCICIO 4----------")

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

def imprimirInformacion(diccionario):
    for clave in diccionario:
        lista = diccionario [clave]
        print(f"{len(lista)} {clave.upper()}")
        print("\n".join(lista))
        print()


imprimirInformacion(costa_rica)
