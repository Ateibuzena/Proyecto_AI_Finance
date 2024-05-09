import streamlit as st
from funciones.funciones_pagina_inicio import *

st.set_page_config(layout = "wide")

df = pd.read_csv("./data/datos.csv")

df = df[["cc_num", "category", "trans_date_trans_time", "amt"]].copy()
df['trans_date_trans_time'] = pd.to_datetime(df['trans_date_trans_time'])
#df['trans_date_trans_time'] = df['trans_date_trans_time'].dt.date
# Dividir la columna 'fecha' en año, mes
# Extraer solo la hora y descartar la información de la fecha
#df['hour'] = df['trans_date_trans_time'].dt.hour
#df['año'] = df['trans_date_trans_time'].dt.year
#df['mes'] = df['trans_date_trans_time'].dt.month

def pagina_inicio():
    
    st.markdown("<span style='display: block; white-space: nowrap; text-align: center; font-size: 100px; font-weight: bold;'>AI Finance</span>", unsafe_allow_html=True)

    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")

    texto = """<div style=' text-align: justify; font-size: 20px;'>
                El Planificador Financiero Departamental 
                es una herramienta integral diseñada para ayudar a las empresas a administrar sus finanzas de manera eficaz, brindando una previsión y un
                sistema de ahorro personalizado para cada departamento o categoría de gastos en sus transacciones.
                </div>"""
    
    # Mostrar el texto alineado al centro
    
    st.markdown(texto, unsafe_allow_html=True)

    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")

    st.markdown("<span style='display: block; white-space: nowrap; text-align: center; font-size: 50px; font-weight: bold;'>Cartera de clientes</span>", unsafe_allow_html=True)

    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")

    columna_1, columna_2, columna_3 = st.columns([1, 0.2, 1])

    with columna_1:
        texto = """<div style=' text-align: justify; font-size: 20px;'>
                Para este proyecto contamos con diferentes tipo de clientes.
                Simulando que somos uno de ellos, podemos seleccionar lo que sería nuestro perfil.
                Cada cliente tiene distintas transacciones y distintas estadísticas.
                </div>"""
    
        # Mostrar el texto alineado al centro
    
        st.markdown(texto, unsafe_allow_html=True)
    
    with columna_3:

        st.markdown(" ")
    
        st.markdown("<span style='display: block; white-space: nowrap; text-align: center; font-size: 25px; font-weight: bold;'>Seleccione una cuenta bancaria:</span>", unsafe_allow_html=True)
        st.markdown(" ")
    
        cuenta = st.selectbox('', df["cc_num"].unique())
        st.markdown(" ")

    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")  
    df_filtrado =  df[df["cc_num"] == cuenta]

    # Calcular la media de gastos diarios
    # Añadir una columna para la suma total de gastos por día
    df_filtrado['Gasto'] = df_filtrado.groupby('trans_date_trans_time')['amt'].transform('sum')
    
    # Añadir un apartado para mostrar la media de gastos
    st.title('Análisis de Gastos')

    c_1,c_3, c_2 = st.columns([1, 0.2, 1])
    with c_1:
    # Mostrar el DataFrame
        st.subheader('DataFrame de Gastos')
        st.write(df_filtrado)

    with c_2:
        # Calcular la media de gastos diarios
        media_diaria = df_filtrado['Gasto'].mean().round(2)
        st.subheader("Media de gastos diarios:")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(f"<span style='display: block; white-space: nowrap; text-align: center; font-size: 100px; font-weight: bold;'>{media_diaria}</span>", unsafe_allow_html=True)
        
    st.markdown("<span style='display: block; white-space: nowrap; text-align: center; font-size: 50px; font-weight: bold;'>¿Cómo se distribuyen tus gastos?</span>", unsafe_allow_html=True)

    st.markdown(" ")
    
    c_1, c_2 = st.columns(2)
    with c_1:
        st.markdown("<span style='display: block; white-space: nowrap; text-align: center; font-size: 25px; font-weight: bold;'>Desde</span>", unsafe_allow_html=True)
        fecha_origen = st.selectbox('', df_filtrado["trans_date_trans_time"].unique())
        st.markdown(" ")

    with c_2:
        st.markdown("<span style='display: block; white-space: nowrap; text-align: center; font-size: 25px; font-weight: bold;'>Hasta</span>", unsafe_allow_html=True)
        fecha_destino = st.selectbox('', df_filtrado[df_filtrado["trans_date_trans_time"] > fecha_origen]["trans_date_trans_time"].unique())
        st.markdown(" ")
    
    df_filtrado_2 = df_filtrado[(df_filtrado["trans_date_trans_time"] >= fecha_origen) & (df_filtrado["trans_date_trans_time"] <= fecha_destino)]
    
    st.plotly_chart(pie_chart(df_filtrado), use_container_width = True)
