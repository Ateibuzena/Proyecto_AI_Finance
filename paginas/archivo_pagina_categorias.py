import streamlit as st
import plotly.express as px
import os
import pandas as pd
import time
import plotly.graph_objects as go
import streamlit as st
import numpy as np
from datetime import datetime, timedelta
import pickle
# Obtener la ruta completa del archivo CSV
ruta_csv = os.path.join(os.getcwd(), "./data/datos.csv")

from datetime import datetime, timedelta

# Fecha inicial y final
fecha_inicial = datetime(2019, 1, 1)
fecha_final = datetime(2020, 12, 31)

# Crear la lista de fechas
lista_fechas = [fecha_inicial + timedelta(days=d) for d in range((fecha_final - fecha_inicial).days + 1)]

# Cargar los datos desde el archivo CSV
def cargar_datos(archivo_csv):
    return pd.read_csv(archivo_csv)

# 1. Gráfico de líneas temporal por categoría y gasto
def line_plot_by_category(cc_num, df_filtered):
    
    fig = go.Figure()
    for category in df_filtered['category'].unique():
        df_category = df_filtered[df_filtered['category'] == category]
        fig.add_trace(go.Scatter(x=df_category['trans_date_trans_time'], y=df_category['amt'],
                                 mode='lines',
                                 name=category))
    fig.update_layout(
                      xaxis_title='Fecha',
                      yaxis_title='Monto')
    return fig

# Definir la página "Categorías"
def pagina_categorias():
    # Cargar los datos
    df = cargar_datos(ruta_csv)
    st.title("Histórico de la Distribución de Gastos por Categorías")

    c_1,c_3, c_2 = st.columns([1, 0.2, 1])
    with c_1:
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        texto = """<div style=' text-align: justify; font-size: 20px;'>
                    En esta sección, te ofrecemos una visión detallada del histórico de tus gastos dentro de una categoría específica. Entendemos lo importante que es tener un control preciso sobre tus finanzas, por eso te brindamos esta herramienta que te permitirá visualizar y analizar tus hábitos de gastos en detalle.
                    </div>"""
        
            # Mostrar el texto alineado al centro
        
        st.markdown(texto, unsafe_allow_html=True)
    with c_2:
        st.markdown(" ")
        st.markdown(" ")
        texto = """<div style=' text-align: justify; font-size: 20px;'>
                    Nuestra gráfica interactiva te muestra la evolución de tus gastos a lo largo del tiempo en la categoría seleccionada. Podrás observar fácilmente cómo han variado tus gastos en esta categoría en función de los días, semanas o meses. Esta información te ayudará a identificar tendencias, establecer presupuestos más realistas y tomar decisiones financieras más informadas.
                    </div>"""
    
        # Mostrar el texto alineado al centro
    
        st.markdown(texto, unsafe_allow_html=True)
    st.markdown(" ")
    st.markdown(" ")
    st.write("Explora el gráfico utilizando las herramientas de interacción, como el zoom y el desplazamiento, para examinar de cerca áreas específicas de interés. Además, puedes personalizar la visualización cambiando el rango de fechas o ajustando los filtros según tus preferencias.")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown("# ¡Comienza a explorar tu historial de gastos ahora mismo y toma el control de tus finanzas de una vez por todas!")
    st.markdown(" ")
    c_1, c_2 = st.columns(2)

    with c_1:
        cuenta = st.selectbox('', df["cc_num"].unique())
        st.markdown(" ")


    with c_2:
        categoria = st.selectbox('', df["category"].unique())
        st.markdown(" ")
    df_cuenta = df[(df["cc_num"] == cuenta) & (df["category"] == categoria)]

    fig = line_plot_by_category(cuenta, df_cuenta)
    # Mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)
    
    df_cuenta = df[df["cc_num"] == cuenta]
    df_cuenta['trans_date_trans_time'] = pd.to_datetime(df_cuenta['trans_date_trans_time'])
    df_cuenta['trans_date_trans_time'] = df_cuenta['trans_date_trans_time'].dt.date
    # Agrupar el DataFrame por 'fecha' y 'categoria', y luego sumar los montos
    df_cuenta = df_cuenta.groupby(['trans_date_trans_time'])['amt'].sum().reset_index()
    # Convertir la columna 'fecha' a tipo datetime si no lo está
    df_cuenta['trans_date_trans_time'] = pd.to_datetime(df_cuenta['trans_date_trans_time'])

    # Obtener las fechas que faltan en el DataFrame
    fechas_faltantes = set(lista_fechas) - set(df_cuenta['trans_date_trans_time'])

    # Crear un DataFrame con las fechas faltantes y un valor de 0
    df_faltantes = pd.DataFrame({'trans_date_trans_time': list(fechas_faltantes), 'amt': 0})

    # Concatenar el DataFrame original con el DataFrame de fechas faltantes
    df_completo = pd.concat([df_cuenta, df_faltantes])

    df_completo = df_completo.groupby(['trans_date_trans_time'])['amt'].sum().reset_index()
    # Ordenar el DataFrame por la columna 'fecha'
    df_completo = df_completo.sort_values(by='trans_date_trans_time')


    # Calcular la suma acumulativa por categoría
    df['gasto_acumulado'] = df.groupby('category')['amt'].cumsum()

    st.title('Gasto Acumulado por Categoría')

    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    texto = """<div style=' text-align: justify; font-size: 20px;'>
                Te presentamos una representación visual del gasto acumulado dentro de una categoría específica a lo largo del tiempo. Comprender cómo evoluciona tu gasto acumulado en una categoría particular es fundamental para mantener un control financiero sólido y tomar decisiones informadas.
                </div>"""
        # Mostrar el texto alineado al centro
    
    st.markdown(texto, unsafe_allow_html=True)
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")

    texto = """<div style=' text-align: justify; font-size: 25px;'>
                Observa de manera intuitiva cómo el gasto total ha ido aumentando o disminuyendo a medida que transcurren los días, semanas o meses. Esta representación te permite identificar tendencias, detectar picos de gasto y evaluar tu progreso hacia tus objetivos financieros.
                </div>"""
        # Mostrar el texto alineado al centro
    
    st.markdown(texto, unsafe_allow_html=True)
    # Crear una figura con Plotly Express
    fig = px.line(df, x= 'trans_date_trans_time', y='gasto_acumulado', color='category')

    # Mostrar la figura en Streamlit
    st.plotly_chart(fig, use_container_width=True)