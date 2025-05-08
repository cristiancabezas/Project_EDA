import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def edad_estudios():
    st.title('👥 Visualización de Edad VS Nivel académico en Badalona')
    with st.expander('PUBLICO OBJETIVO', expanded=False):
        st.markdown('''
        * Principalmente jóves y adultos entre 18 y 45 años
        * Personas con hábitos saludables, deportistas
        * Buscan alimentación saludable
        * Nivel de renta medio o alto, ya que es un producto más caro que lo convencional
        * Nivel de estudios medio o altos
        * Ubicación en zonas urbanas y con buen clima''')
    try:
        df_edad = pd.read_csv('./src/data/poblacion_anio_anio.csv', index_col = 0)
        df_estudios = pd.read_csv('./src/data/edad_y_estudios.csv', index_col = 0)
        fig1, ax1 = plt.subplots()
        ax1.plot(df_edad['Edad'], df_edad['Hombres'], label = 'Hombres')
        ax1.plot(df_edad['Edad'], df_edad['Mujeres'], label = 'Mujeres')
        ax1.set_title('Evolución cantidad de hombres y mujeres')
        ax1.set_xlabel('Edad')
        ax1.set_ylabel('Personas')
        ax1.grid(True)
        ax1.legend()
        st.pyplot(fig1)
        st.write('''
                Este gráfico muestra la evolución de la cantidad de hombres y mujeres según la edad,
                podemos detectar el perfil potencial de clientes. Como se ve, a partir de los 30 años, 
                especialmente entre los 35 y 45 años hay un aumento importante, que se puede ver como hay más hombres por muy poco.
                De cara al marketing para nuestro Açaí tendremos que tenerlo en cuenta, porque dependiendo de la edad, enfocaremos el
                marketing de una forma u otra. Tenemos que considerar que muchas personas empiezan a cuidar más su alimentación y
                estilo de vida a partir de esos dichos 30 años, esta combinación es perfecta para guiarla con un fresco y delicioso Açaí.''')
        fig2, ax2 = plt.subplots()
        suma_educacion = df_estudios[['Educacion Basica', 'Educacion Media', 'Educacion Superior']].sum()
        suma_educacion.plot(kind='pie', startangle = 90, autopct='%1.1f%%')
        ax2.set_title('Distribución nivel de estudio')
        st.pyplot(fig2)
        plt.close()
        st.write('''
                Como vemos en este gráfico la mayoría de la población de Badalona tiene un nivel educativo medio o superior, esto
                nos quiere decir que deberían tener más conciencia sobre hábitos saludables. Como es de pensar, entonces, existe una 
                alineación entre la calidad de posibles potenciales clientes y el posicionamiento del Açaí como una opción atractiva.''')
    except Exception as e:
        st.error(f'❌ Error al cargar los datos: {str(e)}')
if __name__ == '__main__':
    edad_estudios()