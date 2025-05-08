import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def deportistas_centros():
    st.title('🏋️‍♀️ Visualización Deportistas y Centros de deporte en Badalona')
    with st.expander('PUBLICO OBJETIVO', expanded=False):
        st.markdown('''
        * Principalmente jóves y adultos entre 18 y 45 años
        * Personas con hábitos saludables, deportistas
        * Buscan alimentación saludable
        * Nivel de renta medio o alto, ya que es un producto más caro que lo convencional
        * Nivel de estudios medio o altos
        * Ubicación en zonas urbanas y con buen clima''')
    try:
        df_deportistas = pd.read_csv('./src/data/deportistas_bdn.csv', index_col = 0)
        df_centros = pd.read_csv('./src/data/centros_de_deporte_bdn.csv', index_col = 0)
        fig1, ax1 = plt.subplots()
        poblacion_total = df_deportistas['Población'].iloc[0]
        practican = df_deportistas['Personas que practican deporte'].iloc[0]
        no_practican = poblacion_total - practican
        ax1.pie([practican, no_practican], labels = ['Practica deporte', 'No practica'], startangle = 90, autopct='%1.1f%%')
        ax1.set_title('Personas que practican deporte en Badalona')
        ax1.legend(loc='upper left')
        st.pyplot(fig1)
        st.write('''
                Observando el gráfico, se ve que en Badalona, más del 50% de la población practica deporte,
                esto nos dice el tipo de vida activo que llevan y conciencia por la salud de cada uno. Este datos nos abre muchas
                puertas de cara al negocio de Açaí, porque es un producto muy bien valorado por las personas que optan/buscan opciones
                naturales, nutritivas, deliciosas y energéticas.''')
        fig2, ax2 = plt.subplots()
        sns.barplot(data = df_centros, x='2024', y = 'tipo instalacion', ax=ax2)
        ax2.set_xlabel('Cantidad')
        ax2.set_title('Centros de deporte en Badalona')
        st.pyplot(fig2)
        plt.close()
        st.write('''
                En Badalona tenemos mucha infraestructura deportiva, con casi 700 instalaciones deportivas distribuidas por la ciudad
                de Badalona. Esto nos indica que la ciudad promueve un estilo de vida activo. Esto nos sigue afirmando la importancia 
                de una tienda de Açaí en Badalona, siendo un producto saludable y buenísimo para todos los habitantes/turistas.''')
    except Exception as e:
        st.error(f'❌ Error al cargar los datos: {str(e)}')
if __name__ == '__main__':
    deportistas_centros()