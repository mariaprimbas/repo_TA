def mostrar_menu():
  '''
    Función que muestra el menu de opciones disponibles al usuario
    Parameters
    None
    Returns
    None
    '''
  print ("El sistema está orientado a empresas, analistas de marketing, responsables comerciales o investigadores interesados en comprender el comportamiento de compra de sus clientes. A partir de este análisis, el sistema clasifica a los clientes según su perfil y genera recomendaciones que ayudan a diseñar estrategias de marketing, campañas de fidelización y ventas más efectivas.\n ")
  print("MENU DE OPCIONES:\n1.⁠ ⁠Consultar perfil de cliente\n2.⁠ ⁠Mostrar estadísticas generales\n3.⁠ ⁠Comparar segmentos\n4.⁠ ⁠Mostrar gráficos\n5.⁠ ⁠Generar recomendaciones con IA.\n6.⁠ ⁠Visualizar en la interfaz\n7.⁠ ⁠Mostrar mapa geografico\n8⁠. ⁠Salir\n")
  
def pedir_opcion():
    '''
    Función que solicita al usuario una opción del menú y valida
    que sea un número entero entre 1 y 8.

    Returns
    -------
    opcion : int
        Opción válida elegida por el usuario.
    '''

    while True:

        try:
            opcion = int(input("Seleccione una opción (1-8): "))
            if opcion < 1 or opcion > 8:
              print("Error: debe ingresar una opción entre 1 y 8.")
              continue

            return opcion

        except ValueError:
            print("Error: debe ingresar un número entero.")
            continue




def pedir_id_cliente(df):
    '''
    funcion que pide un id de cliente y lo valida

    Parameters
    ----------
    df : DataFrame
        DataFrame con los datos del dataset ya validados.

    Returns
    -------
    id_cliente : int
        el id del cliente pedido ya validado.

    '''

    while True:

        try:

            id_cliente = int(input("Ingrese ID del cliente (n° del 1 al 100.000): "))

            if id_cliente in df["id"].values:
                return id_cliente

            print("Error: no existe un cliente con ese ID")

        except ValueError:

            print("Error: debe ingresar un número")

      
