import streamlit as st
from PIL import Image


def introduccion():
    st.title("Introducción")
    st.markdown('''El açaí es un fruto originario de la Amazonía, reconocido por su alto valor nutricional 
                y sus propiedades antioxidantes. En los últimos años, su demanda ha crecido considerablemente 
                tanto en el mercado local como internacional, convirtiéndose en un producto clave en la economía 
                de varias regiones productoras, especialmente en Brasil.''')
    img = Image.open('./src/img/açai_fruta.jpeg')
    st.image(img, use_container_width=False) #ver si es necesario o queda muy grande
    st.markdown('''- Una de las formas más populares de consumir açaí es el **açaí bowl**:   
                Es una preparación fría a base de pulpa congelada del fruto (açaí),
                acompañado de diferentes topping como la frutas, granola, miel crema de cachuete, entre otros.
                Este plato se ha vuelto muy popular en cafeterías, gimnasios, locales especializados en **Açaí**
                y restaurantes saludables en todo el mundo.''')
    img = Image.open('./src/img/acaibowl.jpeg')
    st.image(img, use_container_width=False)
    st.markdown('''En este EDA vas a encontrar el estudio de las siguientes variables sobre Badalona:  
                - 👥 **Edad** y **Nivel educativo**: características demográficas y formativas de la población.  
                - 💰 **Ingresos** y **Gastos**: evaluación de la situación económica y hábitos de consumo.  
                - 🏋️‍♀️ **Deportistas** y **Centros censados**: medidas de un estilo de vida saludable.  
                - 🌇 **Densidad de población** y **Paro**: situaciones urbanas y laborales.  
                - 🌡️ **Temperatura**: influencia del clima en el consumo de Açaí.  
                - 🍔 **Opciones no saludables**: Entorno desfavorable para la población.  
                - 🚩 **Competencia directa (Badalona)**: Análisis de la competencia local (Badalona).  
                - 🚚 **Competencia en delivery**: Estudio de la competencia en delivery.  
                - 🧱 **Opciones de locales**: Opciónes para llevar a cabo el negocio.''')
    st.write('')
    st.markdown('''
                * El objetivo es encontrar la viabilidad de abrir un negocio de **Açaí** en Badalona, 
                utilizando técnicas de visualización y análisis exploratorio.  
                * Este EDA combina datos sociodemográficos, económicos y de mercado para entender 
                mejor el comportamiento del mercado y facilitar la toma de decisión.''')
    st.markdown("""
                ✅Contáctame por:
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?logo=linkedin)](www.linkedin.com/in/cristian-cabezas-delgado)
    [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/cristiancabezas)
    """, unsafe_allow_html=True)
if __name__ == '__main__':
    introduccion()