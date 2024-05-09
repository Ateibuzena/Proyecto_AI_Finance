import streamlit as st
from funciones.funciones_pagina_prediccion import *
from funciones.funciones_pagina_inicio import *
import matplotlib.pyplot as plt
 



df = pd.read_csv("./data/datos.csv")

def pagina_prediccion():
    
    st.markdown("<span style='display: block; white-space: nowrap; text-align: center; font-size: 50px; font-weight: bold;'>Modelo de Predicción de Gastos Futuros</span>", unsafe_allow_html=True)

    texto = """<div style=' text-align: justify; font-size: 20px;'>
                    Bienvenido a nuestra herramienta de predicción de gastos futuros. En esta sección, te presentamos un modelo avanzado que utiliza técnicas de aprendizaje automático para predecir los gastos financieros futuros con base en datos históricos
                    </div>"""
        
    st.markdown(texto, unsafe_allow_html=True)
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")

    c_1, c_2, c_3 = st.columns([1, 0.2, 1])
    
    with c_1:
        st.markdown("""## ¿Cómo funciona?""")

        st.markdown("""Nuestro modelo de predicción de gastos utiliza datos históricos de transacciones financieras para identificar patrones y tendencias. Luego, emplea algoritmos avanzados para realizar predicciones precisas sobre los gastos futuros. Estas predicciones pueden ayudarte a tomar decisiones financieras informadas y planificar tu presupuesto con anticipación.""")
    with c_3:
        st.markdown("""## Explora tus predicciones""")

        st.markdown("""¡Explora las predicciones de nuestro modelo para entender mejor tus patrones de gastos! Puedes ingresar tus datos financieros actuales y obtener predicciones personalizadas para los próximos meses. Además, nuestra herramienta te permite visualizar gráficamente las predicciones para facilitar la interpretación.""")
    with c_1:
        st.markdown("""## Toma el control de tus finanzas""")

        st.markdown("""Con la información proporcionada por nuestro modelo de predicción de gastos, puedes tomar el control de tus finanzas y planificar tu futuro con confianza. Utiliza nuestras herramientas para optimizar tu presupuesto y alcanzar tus objetivos financieros.""")
    with c_3:
        st.markdown("""# ¡Comienza a explorar y descubre lo que el futuro tiene reservado para tus finanzas!""")
        
    #with c_2:
    #    categoria = st.selectbox('', df["category"].unique())
    #   st.markdown(" ")
    st.markdown("<span style=' text-align: center;display:block; font-size: 50px; font-weight: bold;'>¡ Conoce tus gastos con antelación !</span>", unsafe_allow_html=True)
    
    with st.form('my_form'):
        texto = ("""<div style='text-align: justify; font-sixe: 18px; '>Pulse "predecir" para saber la predicción de gastos de los próximos 10 días""")
        st.markdown(" ")
        st.markdown("## Número de cuenta:")
        cuenta = st.selectbox('', df["cc_num"].unique())
        st.markdown(" ")


        click = st.form_submit_button("Predecir")
        if click: 
            df_filtrado = df[df["cc_num"] == cuenta].copy()
            
            lista = df_filtrado["amt"][-10:].values
            modelo = cargar_modelo(f"data/modelo_{cuenta}.keras")
            dias_a_predecir = 31
            predicciones = predecir_gasto(modelo, dias_a_predecir, lista)
        # Crear la figura de Plotly
            fig = go.Figure()

            # Agregar la serie de datos a la figura
            fig.add_trace(go.Scatter(x=list(range(len(predicciones))), y=predicciones, mode='lines', name='Datos'))

            # Personalizar el diseño de la figura
            fig.update_layout(
                            xaxis_title='Días',
                            yaxis_title='Gasto')

            # Mostrar la figura en Streamlit
            st.plotly_chart(fig)

            st.markdown("")
            st.markdown("")
            
    
    st.write("<span style='display: block; text-align: center; font-size: 20px; font-weight: bold;'>Conoce las métricas de nuestro modelo</span>", unsafe_allow_html=True)
    st.markdown("")
    st.markdown("")
    st.write("<span style='display: block; text-align: center; font-size: 20px; font-weight: bold;'>El rendimiento general del modelo se evalúa mediante la pérdida de validación: si es baja, el modelo funciona bien; si es alta, no. El análisis específico del gráfico indica un buen rendimiento y ausencia de sobreajuste, con la pérdida de validación decreciendo y sin aumentar después de cierto punto.</span>", unsafe_allow_html=True)
    
    c_1, c_2, c_3 = st.columns ([1, 0.2, 1])
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    with c_1:
        texto = ("""<div style='display:block; text-align: center; font-size: 20px;'>
                        Historial de las diferencias absolutas entre las predicciones
                        del modelo y los valores reales durante el entrenamiento""")

        st.markdown(texto,  unsafe_allow_html=True)
        st.plotly_chart(funcion_mse(cuenta))
        st.markdown("")
        st.markdown("")
    with c_3:
        texto = ("""<div style='display:block; text-align: center; font-size: 25px;'>
                        Historial de pérdida durante el entrenamiento""")

        st.markdown(texto,  unsafe_allow_html=True)
        st.plotly_chart(funcion_mae(cuenta))