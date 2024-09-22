def calcular_descuento(monto_total, porcentaje_descuento=15):
    """Calcula el monto del descuento aplicado al monto total."""
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Programa principal
if __name__ == "__main__":
    # Primera llamada: solo monto total
    monto1 = 200
    descuento1 = calcular_descuento(monto1)
    monto_final1 = monto1 - descuento1
    print(f"Monto total: {monto1} | Descuento: {descuento1} | Monto final a pagar: {monto_final1}")

    # Segunda llamada: monto total y porcentaje de descuento
    monto2 = 150
    porcentaje2 = 15
    descuento2 = calcular_descuento(monto2, porcentaje2)
    monto_final2 = monto2 - descuento2
    print(f"Monto total: {monto2} | Descuento: {descuento2} | Monto final a pagar: {monto_final2}")
