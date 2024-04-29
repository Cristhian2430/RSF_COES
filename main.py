import streamlit as st
import pandas as pd

# Título de la aplicación
st.title('Streamlit Application')

# Crear una entrada de texto para que el usuario ingrese una cadena
user_input = st.text_input('Ingrese su texto:', 'EJE - PROGMW')

# Función para eliminar espacios en blanco
def remove_spaces(input_string):
    return input_string.replace(" ", "")

# Llamar a la función y almacenar el resultado
processed_text = remove_spaces(user_input)

# Mostrar el texto procesado
st.write('Texto sin espacios:', processed_text)

# También podríamos mostrar un DataFrame como ejemplo
df = pd.DataFrame({
    'Original Text': [user_input],
    'Processed Text': [processed_text]
})

st.write(df)
