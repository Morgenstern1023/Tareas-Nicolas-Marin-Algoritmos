import random

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

numerosGanadores = [2, 3, 7, 11, 12]
input("Presiona enter para lanzar los dados")
while True:
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    if dado1 + dado2 in numerosGanadores:
        print(f" Ganaste el numero que sacaste fue {dado1 + dado2}")
    else:
        print(f"Perdiste el numero que sacaste fue {dado1 + dado2}")
    input("Presiona enter para volver a lanzar los dados")
