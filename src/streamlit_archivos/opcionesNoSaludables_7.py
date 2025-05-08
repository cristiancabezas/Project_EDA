import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def noSaludable():
    st.title('🍔  Visualización Opciones no saludables en Badalona')
    with st.expander('PUBLICO OBJETIVO', expanded=False):
        st.markdown('''
        * Principalmente jóves y adultos entre 18 y 45 años
        * Personas con hábitos saludables, deportistas
        * Buscan alimentación saludable
        * Nivel de renta medio o alto, ya que es un producto más caro que lo convencional
        * Nivel de estudios medio o altos
        * Ubicación en zonas urbanas y con buen clima''')
    try:
        df_noSaludable = pd.read_csv('./src/data/info_locales_comer_dulce_bdn.csv', index_col = 0)
        df_competencia_bdn = pd.read_csv('./src/data/competencia_badalona.csv', index_col = 0)
        fig, ax = plt.subplots(figsize=(10,6))
        dulce = len(df_noSaludable)
        açai = len(df_competencia_bdn)
        colors = ['lightcoral', 'mediumseagreen']
        ax.pie([dulce, açai], labels = ['Opción no saludable', 'Açaí'], startangle = 60, colors = colors, textprops={'fontsize': 14},autopct='%1.1f%%')
        ax.set_title('Opción no saludable VS Açaí en Badalona')
        ax.legend()
        st.pyplot(fig)
        st.write('''
                En esta gráfica se ve una realidad, sólo el 1% es competencia que tenemos en Badalona de Açaí, mientras el 99% de los locales,
                son alternativas no saludables, que a largo plazo conlleva problemas de salud. Nos damos cuenta que el sector Açaí no está
                explotado en Badalona, significa que es una gran oportunidad para montar el negocio de Açaí y cubrir la demanda creciente
                de productos saludables, deliciosos, refrescantes y energéticos.''')
        plt.close()
    except Exception as e:
        st.error(f'❌ Error al cargar los datos: {str(e)}')
if __name__ == '__main__':
    noSaludable()