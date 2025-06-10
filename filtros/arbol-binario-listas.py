# este es un programa para filtrar candidatos usando un arbol binario
# cada pregunta lleva a otra, segun lo que responde el ususario
# se usan listas anidadas, no objetos ni clases ni nada raro

arbol_candidato = [
    "¿Tiene experiencia laboral?",  # esta es la primera pregunta (nivel 1)

    # si responde que sí
    [
        "¿Conoce el lenguaje Python?",  # pregunta 2 si tiene experiencia
        [
            "¿Tiene titulo universitario?",  # si sabe Python, se pregunta por titulo
            ["Candidato Aprobado (Perfil ideal)", None, None],  # si tiene, es ideal
            ["Candidato Aprobado con capacitación", None, None]  # si no tiene, se capacita
        ],
        [
            "¿Sabe el idioma ingles?",  # si no sabe Python, se pregunta por inglés
            ["Candidato Aprobado para soporte técnico", None, None],
            ["Candidato Rechazado por falta de habilidades clave", None, None]
        ]
    ],

    # si responde que no tiene experiencia
    [
        "¿Esta dispuesto a trabajar presencial?",  # pregunta nivel 2 rama NO
        [
            "¿Tiene título universitario?",  # si acepta trabajar presencial
            ["Candidato Aprobado para pasantía", None, None],
            ["Candidato en evaluación (falta formación)", None, None]
        ],
        ["Candidato Rechazado por falta de experiencia y presencialidad", None, None]  # si no quiere trabajar presencial
    ]
]

# esta funcion recorre el arbol segun las respuestas del usuario
def evaluar_candidato(arbol):
    if arbol is None:  # si no hay nada que evaluar
        return

    # si llegamos a una hoja (final del camino), mostramos el resultado
    if arbol[1] is None and arbol[2] is None:
        print("\n RESULTADO FINAL:")  # aca se muestra el resultado final
        print(arbol[0])
        return

    # se muestra la pregunta actual y se pide respuesta
    respuesta = input(arbol[0] + " (si/no): ").strip().lower() # quita espacios y pasa a minusculas

    # si el ususario pone algo distinto de si o no, se repite la pregunta
    while respuesta not in ("si", "no"):
        print("Por favor respondé con 'si' o 'no'.")  # mensaje de error comun
        respuesta = input(arbol[0] + " (si/no): ").strip().lower()

    # si dijo que si, vamos por la rama izquierda (arbol[1])
    if respuesta == "si":
        evaluar_candidato(arbol[1])  # llamada recursiva
    else:
        evaluar_candidato(arbol[2])  # si no, va por la rama derecha

# aca arranca el programa
print("Evaluador de Candidatos para Entrevista de Trabajo")  # titulo
print("Responda con 'si' o 'no' a las siguientes preguntas:\n")  # instruccion
evaluar_candidato(arbol_candidato)  # se llama la funcion con la raiz del arbol
