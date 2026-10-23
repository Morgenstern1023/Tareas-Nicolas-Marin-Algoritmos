#A partir de los registros de recolección, escriba el código que acumule los kilos por material, determine el material con  mayor total y liste los materiales distintos. Indique qué imprime y explique por qué para una de las dos tareas  conviene un dict y para la otra un set.
#Datos de entrada 
registros = [("vidrio", 12), ("papel", 8), ("vidrio", 5), ("plastico", 20),  ("papel", 14), ("metal", 3), ("plastico", 7), ("vidrio", 9)]

#Acumular los kilos por material
totales = {}
for material, kilos in registros:
    if material in totales:
        totales[material] += kilos
    else:
        totales[material] = kilos

#Determinar el material con mayor total
mayor_material = max(totales, key=totales.get)

#Listar los materiales distintos
materiales_distintos = set(material for material, _ in registros)

print("Totales por material:", totales)
print("Material con mayor total:", mayor_material)
print("Materiales distintos:", materiales_distintos)

#Explicación
#Para acumular los kilos por material conviene un dict porque necesitamos asociar cada material con su total de kilos, lo que permite actualizar y consultar rápidamente.
#Para listar los materiales distintos conviene un set porque solo nos interesa la unicidad de los elementos y no necesitamos asociarlos con ningún valor.
