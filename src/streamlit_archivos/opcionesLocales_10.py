import streamlit as st
import folium
from streamlit_folium import st_folium #visualización del mapa
import pandas as pd

def opcionesLocales():
    st.title('🧱 Visualización Opciones de locales para alquilar')
    with st.expander('PUBLICO OBJETIVO', expanded=False):
        st.markdown('''
        * Principalmente jóves y adultos entre 18 y 45 años
        * Personas con hábitos saludables, deportistas
        * Buscan alimentación saludable
        * Nivel de renta medio o alto, ya que es un producto más caro que lo convencional
        * Nivel de estudios medio o altos
        * Ubicación en zonas urbanas y con buen clima''')
    try:
        df_locales = pd.read_csv('./src/data/locales_alquiler.csv', index_col = 0)
        mapa = folium.Map(location = [41.4480, 2.2475], zoom_start = 15)
        lat = df_locales['latitud'].to_list()
        lon = df_locales['longitud'].to_list()
        grupo = folium.map.FeatureGroup(name="circulo")
        for x, y in zip(lat,lon):
            folium.Marker(location= [x, y], popup = 'LOCAL', icon=folium.Icon(icon = 'building',prefix='fa', color='darkblue')).add_to(mapa)
            grupo.add_child(folium.features.CircleMarker([x,y],radius = 5, color='red', fill = True))
            mapa.add_child(grupo)
        folium.Marker(location= [41.43909, 2.24398], popup = 'COMPETENCIA', icon=folium.Icon(icon = 'cutlery', color='red')).add_to(mapa)
        grupo.add_child(folium.features.CircleMarker([41.43909, 2.24398],radius = 5, color='darkblue', fill = True))
        mapa.add_child(grupo)
        st_folium(mapa, width=700, height=600)
        st.write('''
                En este mapa vemos la localización del único local que actualmente ofrece Açaí en Badalona y es un restaurante healthy
                con amplio menú, marcado en rojo. Por otra parte vemos los iconos azules que son las diferentes opciones de locales
                disponibles en Badalona para alquilar en la zona de más flujo de la ciudad, significa que es una gran oportunidad
                estratégica única. Así que mejores zonas no se pueden pedir para abrir un local de Açaí para satisfacer la alta demanda que 
                hay en Badalona.''')
    except Exception as e:
            st.error(f'❌ Error al cargar los datos: {str(e)}')
if __name__ == '__main__':
    opcionesLocales()