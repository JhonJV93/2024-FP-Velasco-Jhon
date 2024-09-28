# Crear un diccionario con información ficticia
informacion_personal = {
    "nombre": "Jhon Velasco",
    "edad": 31,
    "ciudad": "Duran",
    "profesion": "Policia"
}

# Acceder y modificar el valor asociado con la clave "ciudad"
print("Ciudad antes de modificar:", informacion_personal["ciudad"])
informacion_personal["ciudad"] = "Riobamba"
print("Ciudad después de modificar:", informacion_personal["ciudad"])

# Agregar una nueva clave-valor para "profesion"
informacion_personal["profesion"] = "Ing en tecnologias de la informacion"

# Verificar existencia de la clave "telefono"
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0958614250"

# Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario final
print("Información personal final:", informacion_personal)
