Algoritmo SISTEMA_CLASIFICACION_PRIORIDAD
	Escribir 'Inserte los siguientes datos edad, enfermedad y tiempo de espera'
	Leer edad, enfermedad, tiempo_espera
	prioridad <- 1
	Si edad>60 O edad<18 Entonces
		prioridad <- prioridad+1
	SiNo
		prioridad <- prioridad
	FinSi
	Si enfermedad==urgente Entonces
		prioridad <- prioridad+1
	SiNo
		prioridad <- prioridad
	FinSi
	Si tiempo_espera>30 Entonces
		prioridad <- prioridad+1
	SiNo
		prioridad <- prioridad
	FinSi
	Según prioridad Hacer
		prioridad==1:
			Escribir 'Prioridad Baja'
		prioridad==2:
			Escribir 'Prioridad Media'
		prioridad==3, prioridad>3:
			Escribir 'Prioridad Alta'
	FinSegún
FinAlgoritmo
