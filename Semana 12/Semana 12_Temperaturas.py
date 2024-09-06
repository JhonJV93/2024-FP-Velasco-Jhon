# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 70},
            {"day": "Martes", "temp": 72},
            {"day": "Miércoles", "temp": 75},
            {"day": "Jueves", "temp": 74},
            {"day": "Viernes", "temp": 73},
            {"day": "Sábado", "temp": 78},
            {"day": "Domingo", "temp": 80}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 68},
            {"day": "Martes", "temp": 71},
            {"day": "Miércoles", "temp": 76},
            {"day": "Jueves", "temp": 77},
            {"day": "Viernes", "temp": 74},
            {"day": "Sábado", "temp": 79},
            {"day": "Domingo", "temp": 82}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 71},
            {"day": "Martes", "temp": 73},
            {"day": "Miércoles", "temp": 77},
            {"day": "Jueves", "temp": 75},
            {"day": "Viernes", "temp": 76},
            {"day": "Sábado", "temp": 80},
            {"day": "Domingo", "temp": 83}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 69},
            {"day": "Martes", "temp": 70},
            {"day": "Miércoles", "temp": 74},
            {"day": "Jueves", "temp": 76},
            {"day": "Viernes", "temp": 75},
            {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 81}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 60},
            {"day": "Martes", "temp": 62},
            {"day": "Miércoles", "temp": 64},
            {"day": "Jueves", "temp": 63},
            {"day": "Viernes", "temp": 65},
            {"day": "Sábado", "temp": 67},
            {"day": "Domingo", "temp": 69}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 59},
            {"day": "Martes", "temp": 61},
            {"day": "Miércoles", "temp": 63},
            {"day": "Jueves", "temp": 66},
            {"day": "Viernes", "temp": 68},
            {"day": "Sábado", "temp": 70},
            {"day": "Domingo", "temp": 72}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 61},
            {"day": "Martes", "temp": 62},
            {"day": "Miércoles", "temp": 65},
            {"day": "Jueves", "temp": 67},
            {"day": "Viernes", "temp": 69},
            {"day": "Sábado", "temp": 71},
            {"day": "Domingo", "temp": 73}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 62},
            {"day": "Martes", "temp": 63},
            {"day": "Miércoles", "temp": 66},
            {"day": "Jueves", "temp": 68},
            {"day": "Viernes", "temp": 70},
            {"day": "Sábado", "temp": 72},
            {"day": "Domingo", "temp": 74}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "temp": 85},
            {"day": "Martes", "temp": 87},
            {"day": "Miércoles", "temp": 89},
            {"day": "Jueves", "temp": 90},
            {"day": "Viernes", "temp": 92},
            {"day": "Sábado", "temp": 93},
            {"day": "Domingo", "temp": 95}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 83},
            {"day": "Martes", "temp": 85},
            {"day": "Miércoles", "temp": 88},
            {"day": "Jueves", "temp": 89},
            {"day": "Viernes", "temp": 91},
            {"day": "Sábado", "temp": 92},
            {"day": "Domingo", "temp": 94}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 87},
            {"day": "Martes", "temp": 89},
            {"day": "Miércoles", "temp": 91},
            {"day": "Jueves", "temp": 92},
            {"day": "Viernes", "temp": 94},
            {"day": "Sábado", "temp": 96},
            {"day": "Domingo", "temp": 98}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 84},
            {"day": "Martes", "temp": 86},
            {"day": "Miércoles", "temp": 89},
            {"day": "Jueves", "temp": 90},
            {"day": "Viernes", "temp": 92},
            {"day": "Sábado", "temp": 94},
            {"day": "Domingo", "temp": 96}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
for i, ciudad in enumerate(temperaturas):
    print(f"Ciudad {i + 1}:")
    for j, semana in enumerate(ciudad):
        suma = 0
        for dia in semana:
            suma += dia['temp']
        promedio = suma / len(semana)
        print(f"  Semana {j + 1}: {promedio:.2f}°C")
    print()  # Línea en blanco entre ciudades
