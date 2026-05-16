# Calculadora de reparaciones de vehículos
IVA = 0.12 # valor constante del IVA en Ecuador

while True:
    print("Calculadora de reparaciones de vehículos")
    print(" ")

    # Entrada de datos con validación
    while True: 
        entrada = input("Costo total de repuestos ($): ")
        try:
            costo_repuestos = float(entrada)
            if costo_repuestos < 0:
                print("Por favor, ingrese un valor positivo.")
            else:
                break
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
    
    while True:
        entrada = input("Horas de mano de obra: ")
        try:
            horas = float(entrada)
            if horas < 0:
                print("Por favor, ingrese un valor positivo.")
            else:
                break
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

    while True:
        entrada = input("Tarifa por hora de mano de obra ($): ")
        try:
            tarifa_hora = float(entrada)
            if tarifa_hora < 0:
                print("Por favor, ingrese un valor positivo.")
            else:
                break
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            
    # Cálculo del costo de mano de obra
    mano_de_obra = horas * tarifa_hora
    subtotal = costo_repuestos + mano_de_obra
    valor_iva = subtotal * IVA
    total = subtotal + valor_iva

    # Mostrar resultados
    print("\nResumen de la reparación:")
    print(f"Costo de repuestos: ${costo_repuestos:.2f}")
    print(f"Costo de mano de obra: ${mano_de_obra:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"IVA (12%): ${valor_iva:.2f}")
    print(f"Total a pagar: ${total:.2f}")

    print("")
    respuesta = input("¿Calcular otra reparación? (s/n): ")
    
    if respuesta.lower() == "s":
            print("Iniciando nuevo cálculo...\n")
 
    elif respuesta.lower() == "n":

        print("Gracias por usar la calculadora de reparaciones.")
        print("")
        break
 
    else:
        print("Respuesta no válida. Saliendo del programa.")
        print("    Reiniciando el programa...\n")
