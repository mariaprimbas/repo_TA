import folium
from folium.plugins import HeatMap

def generar_mapa_regiones(df):

    coordenadas = {

        "North": (45,-95),

        "South": (30,-95),

        "East": (40,-75),

        "West": (40,-120)

    }

    df = df.copy()

    df["lat"] = df["region"].map(
        lambda x: coordenadas[x][0]
    )

    df["lon"] = df["region"].map(
        lambda x: coordenadas[x][1]
    )

    conteo = df.groupby(
        ["lat","lon"]
    ).size().reset_index(name="cantidad")

    mapa = folium.Map(

        location=[38,-97],

        zoom_start=4

    )

    HeatMap(

        conteo.values.tolist(),

        radius=40,

        blur=25

    ).add_to(mapa)

    mapa.save("mapa_clientes.html")

    print("Mapa generado correctamente.")
    
    
    
