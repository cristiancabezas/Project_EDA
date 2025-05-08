import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def gastos_ingresos():
    st.title('💰 Visualización de Ingresos y Gastos en Badalona')
    with st.expander('PUBLICO OBJETIVO', expanded=False):
        st.markdown('''
        * Principalmente jóves y adultos entre 18 y 45 años
        * Personas con hábitos saludables, deportistas
        * Buscan alimentación saludable
        * Nivel de renta medio o alto, ya que es un producto más caro que lo convencional
        * Nivel de estudios medio o altos
        * Ubicación en zonas urbanas y con buen clima''')
    try:
        df_ingresos = pd.read_csv('./src/data/renta.csv', index_col = 0)
        df_gastos = pd.read_csv('./src/data/gasto_medio_bdn.csv', index_col = 0)
        fig1, ax1 = plt.subplots()
        ax1.plot(df_ingresos['Fecha'], df_ingresos['Renta Bruta'], label='Ingresos Brutos')
        ax1.plot(df_ingresos['Fecha'], df_ingresos['Renta Disponible'], label='Ingresos Disponibles')
        ax1.set_ylabel('Ingresos Brutos y Disponible')
        ax1.legend()
        ax1.grid(True)
        ax1.set_title('Ingresos en Badalona')
        ax_capita = ax1.twinx() #creamos un segundo eje Y
        ax_capita.plot(df_ingresos['Fecha'], df_ingresos['Renta_per_capita'], label='Renta per cápita', color = 'green' ,linestyle='--')
        ax_capita.set_ylabel('Renta per cápita')
        ax_capita.legend(loc = 'upper right')
        st.pyplot(fig1)
        st.write('''
                Como vemos en este gráfico las rentas (bruta y disponible) hasta ahora muestran un crecimiento constante,
                esto nos quiere decir que hay una mayor capacidad de gasto por persona/familia. Desde este punto de vista
                es una buena oportunidad ofrecer Açaí, ya que, más gente va poder permitirse este manjar, que combina
                un buen valor nutricional con un sabor que invita a repetir una y otra vez.''')
        fig2, ax2 = plt.subplots()
        df_gastos.set_index('Gasto medio (Miles Badalona)', inplace=True)
        df_gastos.plot(kind='pie', y = 'Por persona',startangle = 90, autopct='%1.1f%%', legend=False, ax=ax2)
        ax2.set_title('Distribución de gastos relacionados con el Açaí')
        ax2.set_ylabel('')
        st.pyplot(fig2)
        plt.close()
        st.write('''
                Como podemos observar en este gráfico, más del 50% del gasto se encuentra con alimentos y bebidas no alcohólicas,
                lo que entendemos que es una oportunidad para montar el negocio de Açaí. Otra gran parte va a los restaurantes y hoteles,
                quiere decir que sigue reforzando la idea de si es viable o no el negocio de Açaí, y por último otra parte va para ocio 
                y cultura, aquí en Badalona con el buen tiempo y la buena gente, el ocio es algo muy importante como local y/o turista.''')
    except Exception as e:
        st.error(f'❌ Error al cargar los datos: {str(e)}')
if __name__ == '__main__':
    gastos_ingresos()