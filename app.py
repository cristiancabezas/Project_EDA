import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import streamlit as st
from PIL import Image

from src.streamlit_archivos.introduccion_1 import introduccion
from src.streamlit_archivos.edad_estudios_2 import edad_estudios
from src.streamlit_archivos.ingresos_gastos_3 import gastos_ingresos
from src.streamlit_archivos.deportistas_centrosDeporte_4 import deportistas_centros
from src.streamlit_archivos.densidad_paro_5 import densidad_paro
from src.streamlit_archivos.temperatura_6 import temperatura
from src.streamlit_archivos.opcionesNoSaludables_7 import noSaludable
from src.streamlit_archivos.competenciaDirecta_8 import competenciaDirecta
from src.streamlit_archivos.competenciaDelibery_9 import competenciaDelibery
from src.streamlit_archivos.opcionesLocales_10 import opcionesLocales
from src.streamlit_archivos.conclusiones_11 import conclusion

favicon = Image.open('./src/img/acai.png')
st.set_page_config(page_title='¿Un Açaí en Badalona?', page_icon= favicon)

st.markdown("<h1 style='text-align: center;'>¿Es viable montar un negocio de Açaí en Badalona?</h1>", unsafe_allow_html=True)
st.title('')

st.sidebar.header('Análisis población de Badalona')
st.sidebar.markdown("""
    <style>
        /* Cambiar la flecha en el sidebar (el botón de expandir/contraer) */
        .css-1e9l2r6 button[title='Toggle the sidebar'] {
            background-color: transparent !important;  /* Fondo transparente */
            border: none !important;  /* Sin borde */
            padding: 0 !important;  /* Sin relleno */
        }

        /* Cambiar el icono de la flecha para expandir/contraer */
        .css-1e9l2r6 button[title='Toggle the sidebar'] svg {
            fill: #ff6347 !important;  /* Cambiar color de la flecha (puedes usar cualquier color que desees) */
            transform: scale(1.5);  /* Cambiar tamaño del icono */
        }

        /* Agregar un hover effect si lo deseas */
        .css-1e9l2r6 button[title='Toggle the sidebar']:hover svg {
            fill: #32cd32 !important;  /* Cambiar color cuando pasa el ratón */
        }
    </style>
""", unsafe_allow_html=True)
opcion = st.sidebar.radio(
    "Selecciona un objetivo sobre la población:",
    ["Introducción", "👥 Edad y Estudios", "💰 Ingresos y Gastos", "🏋️‍♀️ Deportistas y Centros de deporte", "🌇 Densidad de población y Paro", 
     "🌡️ Temperatura", "🍔 Opciones no saludables", "🚩 Competencia directa", "🚚 Competencia delibery", "🧱 Opciones de locales", "Conclusiones"])

if opcion == 'Introducción':
    introduccion()
elif opcion == '👥 Edad y Estudios':
    edad_estudios()
elif opcion == '💰 Ingresos y Gastos':
    gastos_ingresos()
elif opcion == '🏋️‍♀️ Deportistas y Centros de deporte':
    deportistas_centros()
elif opcion == '🌇 Densidad de población y Paro':
    densidad_paro()
elif opcion == '🌡️ Temperatura':
    temperatura()
elif opcion == '🍔 Opciones no saludables':
    noSaludable()
elif opcion == '🚩 Competencia directa':
    competenciaDirecta()
elif opcion == '🚚 Competencia delibery':
    competenciaDelibery()
elif opcion == '🧱 Opciones de locales':
    opcionesLocales()
elif opcion == 'Conclusiones':
    conclusion()

st.sidebar.title('')
st.sidebar.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/cristian-cabezas-delgado)")
st.sidebar.markdown("[💻 GitHub](https://github.com/cristiancabezas)")