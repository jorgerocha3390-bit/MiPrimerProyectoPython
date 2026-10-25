"""
Programa 8: Info de mi artista favorito
"""
artista = input("Nombre de tu artista favorito: ")
match artista.lower():
    case "taylor swift" | "taylor":
        print("Artista: Taylor Swift | Género: Pop | Álbum famoso: 1989")
    case "bad bunny":
        print("Artista: Bad Bunny | Género: Reggaeton | Álbum: Un Verano Sin Ti")
    case "peso pluma":
        print("Artista: Peso Pluma | Género: Corridos Tumbados | Hit: AMOR")
    case _:
        print(f"¡{artista} es increíble! No tengo info guardada pero es tu favorito.")