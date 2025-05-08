import streamlit as st
import folium
from streamlit_folium import st_folium #visualización del mapa

def competenciaDelibery():
    st.title('🚚 Visualización Competencia delibery a Badalona')
    with st.expander('PUBLICO OBJETIVO', expanded=False):
        st.markdown('''
        * Principalmente jóves y adultos entre 18 y 45 años
        * Personas con hábitos saludables, deportistas
        * Buscan alimentación saludable
        * Nivel de renta medio o alto, ya que es un producto más caro que lo convencional
        * Nivel de estudios medio o altos
        * Ubicación en zonas urbanas y con buen clima''')
    try:
        latitud = [41.38503686555056, 41.40605036028168, 41.39061885712633, 41.40030003153213, 41.38115827419353,
                41.37734993589503, 41.408911910829204, 41.39528029114262, 41.39986438035696, 41.40244896442019, 
                41.394000291316814, 41.39219049841188, 41.402963974670094, 41.39231900086845, 41.401957237052436, 
                41.38929525438637, 41.40044367013197, 41.44273212199273, 41.44192298135415, 41.392009693098764, 
                41.37769253491968, 41.40682889768143, 41.40042292822174, 41.388279267537044, 41.409281720314794, 
                41.45109033524563, 41.403688366122424, 41.39178739936008]
        longitud = [2.1792700932694253, 2.1794469644349572, 2.1623075221057, 2.171215795121764, 2.187289308612741, 
                    2.190339322104765, 2.1759343564967693, 2.171457952793264,  2.205670577926816, 2.203677739301407, 
                    2.1728650816290402, 2.1689115662853196, 2.1728721917952862, 2.1864506644339867, 2.2008685797782483, 
                    2.165752468136439, 2.203163352793576, 2.200117910468321, 2.1980736393041354, 2.197147898823795, 
                    2.190658623956116, 2.193860833747799, 2.1796146258089815, 2.1650738654019057, 2.1708357301545487, 
                    2.208766795125288, 2.176032637450212, 2.170558552793001]
        mapa = folium.Map(location = [41.41754180238399, 2.21044323146972], zoom_start = 12)
        grupo = folium.map.FeatureGroup(name="circulo")
        for x, y in zip(latitud,longitud):
            folium.Marker(location= [x, y], popup = 'COMPETENCIA', icon=folium.Icon(icon = 'cutlery', color='darkblue')).add_to(mapa)
            grupo.add_child(folium.features.CircleMarker([x,y],radius = 5, color='red', fill = True))
            mapa.add_child(grupo)
        st_folium(mapa, width=700, height=600)
        st.write('''
                Este mapa está nos muestra todos los locales que ofrecen Açaí y llegan a Badalona en formato delivery, 
                como se ve hay una gran concentración en Barcelona ciudad, hay sólo un local en Santa Coloma de Gramenet que
                está relativamente cerca de Badalona (quizás la mejor opción de pedir delivery) hay que pensar que es un producto
                frío con textura, contra más lejos esté el local proveedor, peor calidad vamos a recibir. Nos damos cuenta que Badalona
                es una zona prácticamente nueva para él Açaí, con alta densidad de población, significa que hay un hueco de mercado
                que tenemos que cubrir con nuestro local de delicioso Açaí para cubrir la demanda de Badalona.''')
    except Exception as e:
            st.error(f'❌ Error al cargar los datos: {str(e)}')
if __name__ == '__main__':
    competenciaDelibery()