Algoritmo Adivinador_de_Numeros
	Adivinanza <- 50
	intentos <- 0
	numero_adivinar <- 0
	limite_sup <- 100
	limite_inf <- 1
	Escribir 'Inserte un numero del 1 al 100 y el sistema lo adivinara en 7 intentos o menos'
	Leer numero_adivinar
	Mientras intentos<7 Y Adivinanza<>numero_adivinar Hacer
		Escribir Adivinanza
		intentos <- intentos+1
		Si Adivinanza<numero_adivinar Entonces
			limite_inf <- Adivinanza+1
		SiNo
			limite_sup <- Adivinanza-1
		FinSi
		Adivinanza <- trunc((limite_inf+limite_sup)/2)
	FinMientras
	intentos <- intentos+1
	Escribir 'El numero que pensaste es ', Adivinanza, ' y tarde ', intentos, ' intentos'
FinAlgoritmo
