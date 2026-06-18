NO OLVIDAR DE ENVIAR LA API KEY POR SEPARADO EN LA ENTREGA DEL TRABAJO Y DAR LAS INSTRUCCIONES (Pegar la APIKEY en el archivo recomendaciones\_api.py donde lo pide)



# Trabajo Aplicado: Sistema de Análisis y Perfilado de Clientes



Integrantes:

* Gloria Alderete Cornejo
* Juana Bibiloni
* Maria Primbas
* Emma Pyfrom
* Belén Zarich



#### Descripción



El proyecto consiste en un sistema de análisis y perfilado de clientes a partir de un dataset comportamiento de compra. El programa permitirá obtener estadísticas generales, comparar segmentos de clientes, visualizar información mediante gráficos, clasificar clientes según diferentes perfiles de consumo y la generación de recomendaciones de marketing a partir de una IA. 

El sistema está orientado a empresas, analistas de marketing, responsables comerciales o investigadores interesados en comprender el comportamiento de compra de sus clientes. . A partir de este análisis, el sistema clasifica a los clientes según su perfil y genera recomendaciones que ayudan a diseñar estrategias de marketing, campañas de fidelización y ventas más efectivas. 

 
Informacion detallada sobre el diseño del Trabajo Aplicado se encuentra en el documento "diseño" en la carpeta "docs". Los diagramas del diseño del trabajo se encuentran en la carpeta "diagramas". 




La función de heatmap devuelve un documento HTML que se almacena en la carpeta del repositorio.


#### Requisitos



* Instalar las dependencias del proyecto en la terminal:



pip install -r requirements.txt




* En la línea 16 del archivo datos.py se encuentra la ubicación del archivo csv, si el programa se corre desde Windows se debe corroborar que esta escrita con \\, en cambio, en Mac debería tener /





#### Dependencias



El archivo *requirements.txt* contiene las siguientes librerías:



* pandas
* matplotlib
* seaborn
* folium
* google-genai
* rich
* webbrowser
* streamlit





#### Configuración inicial

##### Configurar la API Key



En el archivo "recomendaciones\_api.py", reemplazar:



API\_KEY = "PEGAR\_ACA\_LA\_API\_KEY"



por la api key que se les envía por mail

