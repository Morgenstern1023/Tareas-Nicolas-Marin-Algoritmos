## Función que recibe una cadena de texto y devuelve la cadena invertida mediante recursión.

def cadena_invertida(cadena):
    if len(cadena) == 0:
        # Caso Base: una cadena vacía se devuelve tal cual
        return ""
    # Caso Recursivo: se toma el último caracter y se concatena con la inversión del resto de la cadena
    return cadena[-1] + cadena_invertida(cadena[:-1])


texto = "Wabi Sabi es el arte de aceptar la imperfeccion"
print(cadena_invertida(texto))