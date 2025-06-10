# este progama crea un arbol genealógico (familiar) usando listas
# el usuario mete los nombres y se forma un arbol binario simple
# si el usuario pone "X" se corta todo, y si deja vacio se pone "No ingresado"

def construir_arbol():
    print("Bienvenido/a al creador de tu árbol genealógico familiar.")
    print("Ingrese (X) si quiere finalizar el programa en cualquier momento.")
    print("Deje vacío un campo si no desea ingresar ese dato.\n")

    # funcion para pedir el dato al ususario (padre, madre, etc)
    def obtener(nombre_campo):
        dato = input(f"{nombre_campo}: ").strip()  # se saca espacios adelante y atras
        if dato.lower() == "x":  # si pone x se termina todo
            print("\nFinalizando ingreso de datos.\n")
            return "X"
        if dato == "":
            return print ("No ingresado")  # si lo deja vacio se pone este texto
        return dato

    # se piden los datos de la persona principal
    yo = obtener("¿Cuál es tu nombre?")
    if yo == "X": return None

    # se piden los datos del padre
    padre = obtener("Nombre del padre")
    if padre == "X": return None

    # se piden los datos de la madre
    madre = obtener("Nombre de la madre")
    if madre == "X": return None

    # ahora los abuelos paternos
    abuelo_paterno = obtener("Nombre del abuelo paterno")
    if abuelo_paterno == "X": return None

    abuela_paterna = obtener("Nombre de la abuela paterna")
    if abuela_paterna == "X": return None

    # y los abuelos maternos
    abuelo_materno = obtener("Nombre del abuelo materno")
    if abuelo_materno == "X": return None

    abuela_materna = obtener("Nombre de la abuela materna")
    if abuela_materna == "X": return None

    # cada nodo tiene la forma: [nombre, hijo_izquierdo, hijo_derecho]
    arbol = [
        yo,
        [padre,  # rama izquierda del arbol
            [abuelo_paterno, None, None],  # hijo izquierdo del padre
            [abuela_paterna, None, None]   # hijo derecho del padre
        ],
        [madre,  # rama derecha del arbol
            [abuelo_materno, None, None],
            [abuela_materna, None, None]
        ]
    ]

    return arbol  # se devuelve el arbol completo


# funcion para mostrar el arbol en forma de ramas (no es grafico pero se entiende)
def imprimir_arbol_bonito(arbol, prefijo="", es_ultimo=True):
    if arbol is None or arbol[0] == "No ingresado":
        return  # si no hay nada no se imprime

    rama = "└── " if es_ultimo else "├── "  # dibuja rama segun si es el ultimo o no
    print(prefijo + rama + str(arbol[0]))

    nuevo_prefijo = prefijo + ("    " if es_ultimo else "│   ")

    # buscamos los hijos (izq y der) solo si tienen datos
    hijos = [n for n in [arbol[1], arbol[2]] if n is not None and n[0] != "No ingresado"]
    for i, hijo in enumerate(hijos):
        es_ultimo_hijo = (i == len(hijos) - 1)
        imprimir_arbol_bonito(hijo, nuevo_prefijo, es_ultimo_hijo)

# ----------- empieza el progama --------------

arbol_familiar = construir_arbol()

if arbol_familiar:
    print("Arbol genealógico generado:\n")
    imprimir_arbol_bonito(arbol_familiar)
else:
    print("No se ingresó información suficiente para construir el árbol.")