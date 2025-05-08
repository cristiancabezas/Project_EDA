import streamlit as st
from PIL import Image

def conclusion():
    st.markdown('''
    # ✅ Conclusiones

    Después de hacer el análisis de las variables socioeconómicas, demográficas y comerciales de Badalona, se pueden comentar los siguientes puntos importantes:

    - 📈 **Perfil de consumo**: Las zonas con mayor proporción de población joven y con estudios medio y/o superiores tienden a seguir hábitos saludables y nuevas tendencias alimenticias como el açaí bowl.

    - 🏋️‍♀️ **Estilo de vida activo**: Hay una relación buena entre la cantidad de centros deportivos y el porcentaje de personas que hacen deporte, lo que indica un contexto ideal para productos saludables como el açaí.

    - 💰 **Capacidad económica**: Las zonas con mayor renta y gasto medio tienen un mayor potencial de consumo más alto.

    - 🔥 **Clima como ventaja**: Las temperaturas cálidas durante la mayor parte del año dan pie a la alta demanda de productos fríos como el açaí bowl.

    - ⚔️ **Competencia y saturación**: La existencia de opciones no saludables, tenemos que tener en cuenta a la hora de elegir la ubicación, aunque tenemos buenas opciones.

    ---

    En resumen, este análisis ayuda a identificar **zonas con alto potencial para montar un negocio de açaí**, así como aspectos clave a tener en cuenta para su éxito, como el perfil demográfico, el estilo de vida, y el entorno competitivo.
    ''')
    st.markdown("""
                ✅Contáctame por:
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?logo=linkedin)](https://www.linkedin.com/in/cristian-cabezas-delgado)
    [![GitHub](https://img.shields.io/badge/GitHub-black?logo=github)](https://github.com/cristiancabezas)
    """, unsafe_allow_html=True)
if __name__ == '__main__':
    conclusion()
