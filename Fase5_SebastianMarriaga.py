#Sebastian Marriaga Rosado
#213022_131
#Ingeniera de telecomunicaciones

# Matriz con 10 películas mas populares. 
Cont_Peliculas =[
    ["The Shawshank Redemption", 1994, 9.3, "Drama"],
    ["El Padrino", 1972, 9.2, "Crimen"],
    ["Batman: El Caballero de la Noche", 2008, 9.0, "Acción"],
    ["El Padrino Parte II", 1974, 9.0, "Crimen"],
    ["12 Hombres en Pugna", 1957, 9.0, "Drama"],
    ["La Lista de Schindler", 1993, 9.0, "Bélico"],
    ["El Señor de los Anillos: El Retorno del Rey", 2003, 9.0, "Fantasía"],
    ["Pulp Fiction", 1994, 8.9, "Crimen"],
    ["El Bueno, el Malo y el Feo", 1966, 8.8, "Aventura"],
    ["El Señor de los Anillos: La Comunidad del Anillo", 2001, 8.8, "Fantasía"]
]

# Se define la función para filtrar títulos, populares y recientes.
def Titulos_Recientes(Videoteca, Umbral_calificacion, Año_limite):
    """Títulos en la videoteca cumplen con los criterios de popularidad y actualidad."""
    Conteo = 0

    for Pelicula in Videoteca:
        Titulo = Pelicula[0]
        Año = Pelicula[1]
        Calificacion = Pelicula[2]
        
        
        if Calificacion >= Umbral_calificacion and Año >= Año_limite:
            Conteo += 1
            print(f"{Titulo} (Año: {Año}, Calificación: {Calificacion})")
    
    return Conteo

# Se comienzan los print para mostrar resultados.
print("!!Bienvenido a la videoteca digital.¡¡")

# Se solicita a usuario calificacion y el año de la pelicula a filtrar.
Umbral_calificacion = float(input("Ingrese la calificación umbral en decimal: "))
Año_limite = int(input("Ingrese el año límite: "))

# Se muestran los titulos encontrados
print("\nTítulos populares y recientes encontrados:")
Resultado = Titulos_Recientes(Cont_Peliculas, Umbral_calificacion, Año_limite)

# Se muestran la cantidad de total encontrados
print(f"\nTotal de títulos que cumplen los criterios: {Resultado}")