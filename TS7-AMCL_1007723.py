#Ts progra, 21/09/2023, Angie López 

TUPU = True
while TUPU:
    print ("Angie Mariela López Cantoral")

    numero = int(input("Eliga un número del 1 al 10 "))

    if numero < 1 or numero > 10: 
       print("No cumple con el rango")
    else:
        for i in range(1, 11):
            a = i * numero
            print(numero, "x", i, "=", a)
    
    opcion = input("Desea generar otra tabla (Si, No)")
    
    if opcion == "Si": 
        TUPU = True
    
    else:
        opcion == "No"
        TUPU = False

