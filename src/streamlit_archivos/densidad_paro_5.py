import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def densidad_paro():
    st.title('🌇 Visualización Densidad de población y Paro en Badalona')
    with st.expander('PUBLICO OBJETIVO', expanded=False):
        st.markdown('''
        * Principalmente jóves y adultos entre 18 y 45 años
        * Personas con hábitos saludables, deportistas
        * Buscan alimentación saludable
        * Nivel de renta medio o alto, ya que es un producto más caro que lo convencional
        * Nivel de estudios medio o altos
        * Ubicación en zonas urbanas y con buen clima''')
    try:
        df_densidad = pd.read_csv('./src/data/densidad_poblacion_bdn.csv', index_col =0)
        df_paro = pd.read_csv('./src/data/paro_bdn.csv', index_col = 0)
        fig1, ax1 = plt.subplots(figsize = (10,6))
        ax1.plot(df_densidad['Anio'], df_densidad['Densitat (hab./km²)'],marker = 'o', label = 'Densidad poblacional')
        props_flecha = {'arrowstyle' : '->','connectionstyle' : 'arc3','color' : 'red','linewidth' : 2}
        props_flecha2 = {'arrowstyle' : '->','connectionstyle' : 'arc3','color' : 'green','linewidth' : 2}
        ax1.annotate('Crecimiento notable', xy = (2024.5,10655), xytext = (2014.5,10100), arrowprops= props_flecha)
        ax1.annotate('(A futuro)', xy = (2015.5,10067))
        ax1.annotate('Crecimiento notable', xy = (2005.5,10450), xytext = (1996.9,9965), arrowprops= props_flecha2)
        ax1.annotate('(A presente)', xy = (1998,9930))
        ax1.legend()
        ax1.grid(True)
        ax1.set_title('Densidad poblacional Badalona')
        ax1.set_xlabel('Año')
        ax1.set_ylabel('Personas por ($km^2$)')
        st.pyplot(fig1)
        st.write('''
                Como se observa, han habido dos crecimientos notables en los últimos años, esto es bueno para nuestro negocio de Açaí, 
                porque a mayor población mayor mercado para poder ofrecerles nuestro Açaí delicioso y fresquito. De hecho como vemos el 
                primer crecimiento, será público que tendremos ahora y en los siguientes años, y de cara a más de 10 años vista, 
                tendremos el segundo crecimiento (flecha roja), ya que son menores de 18 años ahora mismo.''')
        fig2, ax2 = plt.subplots()
        sns.barplot(data = df_paro, x='Anio', y = 'Total', hue = 'Anio' , legend = False, palette = sns.color_palette('Blues', n_colors=len(df_paro['Total'])), ax=ax2)
        ax2.set_title('Evolución del paro en Badalona')
        ax2.set_ylabel('Población')
        ax2.set_xlabel('Año')
        ax2.tick_params(axis='x', rotation=35)
        st.pyplot(fig2)
        plt.close()
        st.write('''
                Podemos ver la evolución del paro de manera descendente en Badalona. El detonante más complicado fue en 2007-2008, la
                tendencia está siendo descendente después de ese suceso, lo entendemos como una recuperación positiva. Esta gráfica es
                buena para nosotros, ya que a menor paro, indica que hay más empleo y más poder adquisitivo, lo que se traduce en que 
                más personas podrán consumir nuestro Açaí sin problema.''')
    except Exception as e:
        st.error(f'❌ Error al cargar los datos: {str(e)}')
if __name__ == '__main__':
    densidad_paro()