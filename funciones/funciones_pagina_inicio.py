import pandas as pd
import time
import plotly.graph_objects as go
import streamlit as st
import numpy as np
from datetime import datetime, timedelta
import pickle
import keras
from tensorflow.keras.models import load_model

def pie_chart(df_filtered):
    
    fig = go.Figure(data=[go.Pie(labels=df_filtered['category'], values=df_filtered['amt'])])
    return fig

# Función para cargar el modelo desde un archivo pickle
def cargar_modelo(nombre_archivo):
    # with open(nombre_archivo, 'rb') as archivo:
    modelo = keras.models.load_model(nombre_archivo)
        
    return modelo

df = pd.read_csv("./data/datos.csv")
# Función para preparar los datos del día actual
def preparar_datos(lista):
    
    lista = lista[-10: ]# Adaptar según el formato de tus datos
    return np.array(lista)

# Función para obtener la predicción del gasto
def obtener_prediccion(modelo, lista):
    ultima_prediccion = modelo.predict(lista.reshape(1, -1))

    return ultima_prediccion[0][0]

# Función para predecir el gasto del día actual y los siguientes X días
def predecir_gasto(modelo, dias_a_predecir, lista):
    
    # Convertir la fecha actual a formato datetime
    #fecha_actual_dt = datetime.strptime(fecha_actual, "%Y-%m-%d")

    # Predecir el gasto para el día actual
    datos_dia_actual = preparar_datos(lista)
    predicciones = np.concatenate((datos_dia_actual, obtener_prediccion(modelo, datos_dia_actual)))

    # Predecir los siguientes días
    for _ in range(dias_a_predecir - 1):
        # Avanzar un día en la fecha
        #fecha_actual_dt += timedelta(days=1)
        # Convertir la nueva fecha a formato string
        #fecha_actual = fecha_actual_dt.strftime("%Y-%m-%d")

        # Obtener el nuevo día del mes
        #dia_semana_actual = fecha_actual_dt.strftime("%A")

        # Preparar los datos para el próximo día (fecha y día de la semana)
        datos_dia_actual = preparar_datos(predicciones)
        predicciones = np.concatenate((predicciones, obtener_prediccion(modelo, datos_dia_actual)))

    return predicciones


