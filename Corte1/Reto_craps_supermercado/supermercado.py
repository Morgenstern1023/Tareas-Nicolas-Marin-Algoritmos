import random

indiceBola = random.randint(0, 3)
colores = ["Roja", "Azul", "Amarilla", "Blanca"]
compra = float(input("Por favor inserte cuanto fue el valor de su compra: "))

if compra >= 50000:
    input("Felicidades, usted puede hacer un giro para ganar un descuento, dele enter para girar" )
    indiceBola = random.randint(0, 3)
    print(f"La bola seleccionada es: {colores[indiceBola]}")
    if indiceBola == 0:
        print("Ha ganado un descuento del 10%")
        compra = compra * 0.9
    elif indiceBola == 1:
        print("Ha ganado un descuento del 30%")
        compra = compra * 0.7
    elif indiceBola == 2:
        print("Ha ganado un descuento del 50%")
        compra = compra * 0.5
    elif indiceBola == 3:
        print("Ha ganado un descuento del 100%")
        compra = 0
else:
    print("Lo sentimos, no puede participar en la promoción.")
    
print(f"El valor final de su compra es: {compra}")