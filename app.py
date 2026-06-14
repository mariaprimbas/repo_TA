import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from src.datos import cargar_dataset, validar_dataset
from src.metricas import obtener_estadisticas_generales
from src.perfiles import crear_cliente_id, Cliente

st.set_page_config(
    page_title="PulseLab Analytics",
    layout="wide"
)

st.title("📊 Sistema de Análisis y Perfilado de Clientes")

# -------------------
# CARGA DATOS
# -------------------

try:
    df = cargar_dataset()
    df = validar_dataset(df)

except Exception as e:
    st.error(str(e))
    st.stop()

# -------------------
# MENU
# -------------------

opcion = st.sidebar.selectbox(
    "Seleccione una opción",
    [
        "Perfil de cliente",
        "Estadísticas generales",
        "Comparar segmentos",
        "Gráficos"
    ]
)

# -------------------
# PERFIL
# -------------------

if opcion == "Perfil de cliente":

    st.header("Perfil de Cliente")

    id_cliente = st.selectbox(
        "Seleccione un cliente",
        sorted(df["id"].unique())
    )

    cliente = crear_cliente_id(df, id_cliente)

    st.success(cliente.mostrar_resultado())

    st.write("### Datos del cliente")

    st.write({
    "ID": int(cliente.id),
    "Edad": int(cliente.age),
    "Ingreso": int(cliente.income),
    "Frecuencia": cliente.purchase_frequency,
    "Monto compra": int(cliente.purchase_amount),
    "Satisfacción": int(cliente.satisfaction_score)
})

# -------------------
# ESTADISTICAS
# -------------------

elif opcion == "Estadísticas generales":

    st.header("Estadísticas Generales")

    metricas = obtener_estadisticas_generales(df)

    st.dataframe(metricas)

# -------------------
# SEGMENTOS
# -------------------

elif opcion == "Comparar segmentos":

    st.header("Comparación de Segmentos")

    criterio = st.selectbox(
        "Seleccione comparación",
        [
            "Compra promedio según región",
            "Compra promedio según fidelización",
            "Satisfacción promedio según fidelización",
            "Compra promedio según promociones"
        ]
    )

    if criterio == "Compra promedio según región":

        analisis = (
            df.groupby("region")
            .agg(
                compra_promedio=("purchase_amount","mean"),
                cantidad_clientes=("id","count")
            )
            .sort_values("compra_promedio", ascending=False)
        )

    elif criterio == "Compra promedio según fidelización":

        analisis = (
            df.groupby("loyalty_status")
            .agg(
                compra_promedio=("purchase_amount","mean"),
                cantidad_clientes=("id","count")
            )
            .sort_values("compra_promedio", ascending=False)
        )

    elif criterio == "Satisfacción promedio según fidelización":

        analisis = (
            df.groupby("loyalty_status")
            .agg(
                satisfaccion_promedio=("satisfaction_score","mean"),
                cantidad_clientes=("id","count")
            )
            .sort_values("satisfaccion_promedio", ascending=False)
        )

    else:

        analisis = (
            df.groupby("promotion_usage")
            .agg(
                compra_promedio=("purchase_amount","mean"),
                cantidad_clientes=("id","count")
            )
            .sort_values("compra_promedio", ascending=False)
        )

    st.dataframe(analisis)

    st.bar_chart(analisis.iloc[:,0])

# -------------------
# GRAFICOS
# -------------------


elif opcion == "Gráficos":

    st.header("Visualizaciones")

    grafico = st.selectbox(
        "Seleccione gráfico",
        [
            "Compra promedio por fidelización",
            "Distribución de clientes por región"
        ]
    )

    if grafico == "Compra promedio por fidelización":

        fig, ax = plt.subplots(figsize=(8,5))

        datos = df.groupby("loyalty_status")["purchase_amount"].mean().reset_index()

        sns.barplot(
            data=datos,
            x="loyalty_status",
            y="purchase_amount",
            palette="viridis",
            ax=ax
        )

        ax.set_title("Compra promedio por fidelización")
        ax.set_xlabel("Fidelización")
        ax.set_ylabel("Compra promedio")

        ax.grid(axis="y", linestyle="--", alpha=0.3)

        st.pyplot(fig)

    else:

        fig, ax = plt.subplots(figsize=(8,5))

        datos = df["region"].value_counts().reset_index()
        datos.columns = ["region", "count"]

        sns.barplot(
            data=datos,
            x="region",
            y="count",
            palette="magma",
            ax=ax
        )

        ax.set_title("Distribución de clientes por región")
        ax.set_xlabel("Región")
        ax.set_ylabel("Cantidad")

        ax.tick_params(axis='x', rotation=30)

        ax.grid(axis="y", linestyle="--", alpha=0.3)

        st.pyplot(fig)
