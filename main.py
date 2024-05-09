import streamlit as st


from paginas.archivo_pagina_inicio import *
from paginas.archivo_pagina_prediccion import *
from paginas.archivo_pagina_categorias import *

def main():
    
    seleccion_pagina = st.sidebar.radio(label = " ", options = ["Inicio", "Predicción", "Categorías"])
    if seleccion_pagina == "Inicio":
        pagina_inicio()
        
    if seleccion_pagina == "Predicción":
        pagina_prediccion()

    if seleccion_pagina == "Categorías":
        pagina_categorias()
    
if __name__ == "__main__":
    main()