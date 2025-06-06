# Árbol binario representado con listas para filtrar candidatos

arbol_candidato = [
    "¿Tiene experiencia laboral?",  # Nivel 1

    # Rama si
    [
        "¿Conoce el lenguaje Python?",  # Nivel 2
        [
            "¿Tiene titulo universitario?",  # Nivel 3
            ["Candidato Aprobado (Perfil ideal)", None, None],
            ["Candidato Aprobado con capacitación", None, None]
        ],
        [
            "¿Sabe el idioma ingles?",  # Nivel 3 alternativa
            ["Candidato Aprobado para soporte técnico", None, None],
            ["Candidato Rechazado por falta de habilidades clave", None, None]
        ]
    ],

    # Rama no
    [
        "¿Esta dispuesto a trabajar presencial?",  # Nivel 2
        [
            "¿Tiene título universitario?",  # Nivel 3
            ["Candidato Aprobado para pasantía", None, None],
            ["Candidato en evaluación (falta formación)", None, None]
        ],
        ["Candidato Rechazado por falta de experiencia y presencialidad", None, None]
    ]
]

# Funcion recursiva para recorrer el árbol
def evaluar_candidato(arbol):
    if arbol is None:
        return

    # Si es nodo hoja (sin hijos), muestra el resultado final
    if arbol[1] is None and arbol[2] is None:
        print("\n RESULTADO FINAL:")
        print(arbol[0])
        return

    # Mostrar la pregunta actual y pedir respuesta
    respuesta = input(arbol[0] + " (si/no): ").strip().lower()

    # Validación: solo se aceptan "si" o "no"
    while respuesta not in ("si", "no"):
        print("Por favor respondé con 'si' o 'no'.")
        respuesta = input(arbol[0] + " (si/no): ").strip().lower()

    # Elegir rama izquierda (si) o derecha (no)
    if respuesta == "si":
        evaluar_candidato(arbol[1])
    else:
        evaluar_candidato(arbol[2])

# Inicio del programa
print("Evaluador de Candidatos para Entrevista de Trabajo")
print("Responda con 'si' o 'no' a las siguientes preguntas:\n")
evaluar_candidato(arbol_candidato)
