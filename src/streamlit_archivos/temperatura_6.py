import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def temperatura():
    st.title('🌡️  Visualización Temperatura en Badalona')
    with st.expander('PUBLICO OBJETIVO', expanded=False):
        st.markdown('''
        * Principalmente jóves y adultos entre 18 y 45 años
        * Personas con hábitos saludables, deportistas
        * Buscan alimentación saludable
        * Nivel de renta medio o alto, ya que es un producto más caro que lo convencional
        * Nivel de estudios medio o altos
        * Ubicación en zonas urbanas y con buen clima''')
    try:
        df_temperatura = pd.read_csv('./src/data/temperatura_bdn.csv', index_col = 0)
        fig1, ax1 = plt.subplots()
        df_temperatura['Fecha'] = pd.to_datetime(df_temperatura['Fecha'])
        df_temperatura.set_index('Fecha')
        ax1.plot(df_temperatura.index, df_temperatura['T. media'], label='T. media')
        ax1.plot(df_temperatura.index, df_temperatura['T. minima'], label='T. minima')
        ax1.plot(df_temperatura.index, df_temperatura['T. maxima'], label='T. maxima')
        ax1.legend()
        ax1.grid(True)
        ax1.set_title('Distribución de temperatura en Badalona (año)')
        ax1.set_xlabel('Días')
        ax1.set_ylabel('Temperatura (Celsius)')
        st.pyplot(fig1)
        st.write('''
                Como vemos en la gráfica, los meses más cálidos són todos menos invierno, concentrándose en verano, es
                un buen dato para nuestro local de Açaí. En Badalona, encontramos temperaturas que superan los 20º fácilmente,
                acompañado del sol, que siempre está, el consumo de productos refrescantes y encima saludables como el Açaí,
                son clave para combatir las temperaturas.''')
        fig2, ax2 = plt.subplots()
        sns.histplot(df_temperatura['Precipitacion'], ax=ax2)
        ax2.set_ylim(None, 100)
        ax2.set_title('Precipitaciones en Badalona (año)')
        ax2.set_xlabel('Cantidad de lluvia (mm)')
        ax2.set_ylabel('Registro cantidad de lluvia (días)')
        st.pyplot(fig2)
        plt.close()
        st.write('''
                Observando la gráfica, la mayoría de los días en Badalona son secos o con muy poca lluvia. Esto es buen dato
                para nuestro local de Açaí ya que es un producto que se tiende a consumir con el buen tiempo como el de Badalona.
                Esta condición climática que tenemos es genial para atraer a más clientes a consumir nuestro Açaí refrescante y nutritivo.''')
    except Exception as e:
        st.error(f'❌ Error al cargar los datos: {str(e)}')
if __name__ == '__main__':
    temperatura()