def calcular_temperatura_promedio(temperaturas):
    """
    Calcula la temperatura promedio para cada ciudad y semana.

    Parámetros:
    temperaturas (list): Una matriz 3D donde la primera dimensión es ciudades, la segunda es semanas,
                          y la tercera es días, cada uno conteniendo un diccionario con la temperatura del día.

    Retorna:
    dict: Un diccionario donde las claves son los índices de las ciudades y los valores son diccionarios
          que contienen el promedio de temperatura para cada semana de esa ciudad.
    """
    promedios_por_ciudad = {}

    # Iterar sobre cada ciudad
    for i, ciudad in enumerate(temperaturas):
        promedios_por_ciudad[f"Ciudad {i + 1}"] = {}

        # Iterar sobre cada semana en la ciudad
        for j, semana in enumerate(ciudad):
            suma_total = 0

            # Sumar las temperaturas de la semana
            for dia in semana:
                suma_total += dia['temp']

            # Calcular el promedio para la semana
            promedio = suma_total / len(semana) if semana else 0
            promedios_por_ciudad[f"Ciudad {i + 1}"][f"Semana {j + 1}"] = promedio

    return promedios_por_ciudad


# Ejemplo de uso
temperaturas = [
    [  #    QUITO
        [  # Semana 1
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 12},
            {"day": "Viernes", "temp": 21},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp": 19}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 12},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 11},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 16}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 5},
            {"day": "Martes", "temp": 10},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 20}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 12},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 19},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 10}
        ]
    ],
    [  # GUAYAQUIL
        [  # Semana 1
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 20},
            {"day": "Domingo", "temp": 26}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 33},
            {"day": "Miércoles", "temp": 35},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 21},
            {"day": "Domingo", "temp": 22}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 35},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 19},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 13}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 20},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 34}
        ]
    ],
    [  # CUENCA
        [  # Semana 1
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 23},
            {"day": "Domingo", "temp": 25}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 13},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 11},
            {"day": "Sábado", "temp": 12},
            {"day": "Domingo", "temp": 14}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 11},
            {"day": "Jueves", "temp": 12},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 18}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 26}
        ]
    ]
]

# Calcular y mostrar el promedio de temperaturas
promedios = calcular_temperatura_promedio(temperaturas)
for ciudad, semanas in promedios.items():
    print(f"{ciudad}:")
    for semana, promedio in semanas.items():
        print(f"  {semana}: {promedio:.2f}°C")
    print()  # Línea en blanco entre ciudades
