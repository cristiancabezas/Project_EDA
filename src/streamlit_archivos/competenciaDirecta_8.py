import streamlit as st
import folium
from streamlit_folium import st_folium #visualización del mapa

def competenciaDirecta():
    st.title('🚩 Visualización Competencia directa en Badalona')
    with st.expander('PUBLICO OBJETIVO', expanded=False):
        st.markdown('''
        * Principalmente jóves y adultos entre 18 y 45 años
        * Personas con hábitos saludables, deportistas
        * Buscan alimentación saludable
        * Nivel de renta medio o alto, ya que es un producto más caro que lo convencional
        * Nivel de estudios medio o altos
        * Ubicación en zonas urbanas y con buen clima''')
    try:
        mapa = folium.Map(location = [41.4480, 2.2475], zoom_start = 14)
        folium.Marker(location= [41.43909, 2.24398], popup = 'COMPETENCIA', icon=folium.Icon(icon = 'cutlery', color='darkblue')).add_to(mapa)
        grupo = folium.map.FeatureGroup(name="Área de Competencia")
        grupo.add_child(folium.features.CircleMarker([41.43909, 2.24398],radius = 5, color='red', fill = True))
        mapa.add_child(grupo)
        st_folium(mapa, width=700, height=600)
        st.write('''
                Vemos el mapa casi vacío, sí, es la única ubicación exacta del establecimiento que actualmente ofrece Açaí en Badalona,
                que de hecho es un restaurante healthy con un amplio menú. Su localización es en el límite de la ciudad, tocando el puerto,
                quiere decir que tenemos toda Badalona para cubrir ese público con nuestro local de delicioso Açaí. La baja competencia
                nos brinda una oportunidad para posicionarnos en Badalona, ofreciendo un producto saludable, delicioso, refrescante
                y energético en un mercado con potencial de crecimiento cómo Badalona.''')
    except Exception as e:
        st.error(f'❌ Error al cargar los datos: {str(e)}')
if __name__ == '__main__':
    competenciaDirecta()