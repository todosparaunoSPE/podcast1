# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 18:38:02 2025

@author: jperezr
"""

import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Podcast de Finanzas Juveniles", layout="wide")

# Sidebar: Descripción del podcast
st.sidebar.title("Acerca del Podcast")
st.sidebar.markdown("""
**Podcast: Finanzas con Enfoque Juvenil**

En este episodio, abordamos el tema del ahorro para el retiro, algo fundamental para garantizar un futuro financiero estable. 

Temas principales:
1. Introducción al Ahorro para el Retiro.
2. El Poder del Ahorro Temprano: Interés Compuesto.

Exploramos cómo empezar temprano puede marcar una gran diferencia, gracias al interés compuesto y estrategias simples para ahorrar.

### Desarrollado por: 
- Javier Horacio Pérez Ricárdez    
""")

# Título principal
st.title("Podcast: Introducción al Ahorro para el Retiro")
st.markdown("""
¡Bienvenidos! Escucha nuestro último episodio y aprende por qué el ahorro para el retiro es clave desde temprana edad.

Temas cubiertos:
- ¿Qué es el retiro y por qué es importante ahorrar desde jóvenes?
- Cómo el interés compuesto puede trabajar a tu favor.
""")

# Cargar el archivo de podcast automáticamente
podcast_file = "podcast1.mp3"  # Nombre del archivo

try:
    with open(podcast_file, "rb") as audio_file:
        st.audio(audio_file.read(), format="audio/mp3")
        st.success("¡Disfruta el episodio!")
except FileNotFoundError:
    st.error(f"No se encontró el archivo '{podcast_file}'. Por favor, asegúrate de que esté en el mismo directorio que este script.")