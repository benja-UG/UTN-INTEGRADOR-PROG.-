# este progama crea un arbol binario de numeros
# el ususario mete numeros separados por coma y se agregan al arbol

# funcion para insertar numeros al arbol
def insertar(nodo, valor):
    if nodo == None:
        return [valor, None, None]  # si no hay nodo, se crea uno nuevo
    if valor < nodo[0]:
        nodo[1] = insertar(nodo[1], valor)  # va a la izquierda si es menor
    else:
        nodo[2] = insertar(nodo[2], valor)  # va a la derecha si no es menor
    return nodo

# recorrido inorden, osea izquierda - raiz - derecha
def inorden(nodo):
    if nodo == None:
        return []
    return inorden(nodo[1]) + [nodo[0]] + inorden(nodo[2])

# preorden = raiz - izquierda - derecha
def preorden(nodo):
    if nodo == None:
        return []
    return [nodo[0]] + preorden(nodo[1]) + preorden(nodo[2])

# postorden = izquierda - derecha - raiz
def postorden(nodo):
    if nodo == None:
        return []
    return postorden(nodo[1]) + postorden(nodo[2]) + [nodo[0]]

# pedir al usuario que ponga los numeros
print("Arbol Binario de Busqueda")
entrada = input("Ingrese los numeros separados por coma (ej: 5, 3, 8, 2): ")

# pasamos los numeros a una lista (separamos por coma y convertimos a int)
numeros = [int(x.strip()) for x in entrada.split(",") if x.strip().isdigit()]

# ahora creamos el arbol con esos numeros
arbol = None
for num in numeros:
    arbol = insertar(arbol, num)  # se insertan uno por uno

# pedir al usuario que tipo de recorrido quiere
print("Tipos de recorrido: inorden / preorden / postorden")
modo = input("¿Cual queres usar?: ").strip().lower()

# segun lo que elija el usuario, hacemos el recorrido
if modo == "inorden":
    resultado = inorden(arbol)
elif modo == "preorden":
    resultado = preorden(arbol)
elif modo == "postorden":
    resultado = postorden(arbol)
else:
    resultado = []
    print("No entendi ese modo.")

# mostramos el resultado si hay algo para mostrar
if resultado:
    print("El resultado del recorrido es:")
    print(resultado)
else:
    print("No se pudo mostrar el recorrido.")