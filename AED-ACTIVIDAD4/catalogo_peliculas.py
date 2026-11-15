# Actividad 4.4 - Catalogo de peliculas
peliculas = [
    {"titulo": "Inception", "director": "Nolan", "anio": 2010, "genero": "Sci-Fi", "duracion": 148},
    {"titulo": "Toy Story", "director": "Lasseter", "anio": 1995, "genero": "Animacion", "duracion": 81},
    {"titulo": "Avengers", "director": "Whedon", "anio": 2012, "genero": "Accion", "duracion": 143},
    {"titulo": "Coco", "director": "Unkrich", "anio": 2017, "genero": "Animacion", "duracion": 105}
]

def filtrar_por_genero(genero):
    return [p for p in peliculas if p["genero"].lower() == genero.lower()]

def filtrar_por_anio(anio):
    return [p for p in peliculas if p["anio"] > anio]

def ordenar_por_duracion(asc=True):
    return sorted(peliculas, key=lambda x: x["duracion"], reverse=not asc)

def duracion_promedio():
    return sum(p["duracion"] for p in peliculas) / len(peliculas)

# Pruebas
print("Filtrar por Animacion:", filtrar_por_genero("Animacion"))
print("Peliculas despues de 2010:", filtrar_por_anio(2010))
print("Orden ascendente por duracion:", ordenar_por_duracion(True))
print(f"Duracion promedio: {duracion_promedio():.1f} min")