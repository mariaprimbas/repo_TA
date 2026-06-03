import pandas as pd
def obtener_estadisticas_generales(df):
  '''
    Calcula estadísticas generales del dataset de clientes.

    Parameters
    ----------
    df : DataFrame

        DataFrame validado con los datos de clientes.

    Returns
    -------
    df_metricas : DataFrame

        DataFrame con las métricas generales calculadas.
    '''


  cantidad_clientes = df.shape[0]

  edad_promedio = df["age"].mean()

  ingreso_promedio = df["income"].mean()

  compra_promedio = df["purchase_amount"].mean()

  satisfaccion_promedio = df["satisfaction_score"].mean()

  df_metricas = pd.DataFrame({

    "Cantidad clientes":[cantidad_clientes],

    "Edad promedio":[edad_promedio],

    "Ingreso promedio":[ingreso_promedio],

    "Compra promedio":[compra_promedio],

    "Satisfacción promedio":[satisfaccion_promedio]

})
  return df_metricas



