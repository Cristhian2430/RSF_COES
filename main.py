import streamlit as st
import pandas as pd

st.set_page_config(page_title   = "RSF", 
                   page_icon    = ":syringe:",
                   layout       = "wide")

st.title('Reserva Secundaria de Frecuencia (RSF)')

ruta_trabajo = st.text_input('Ingrese la ruta de trabajo donde desea guardar los archivos:', '')


# Mostrar el texto procesado
st.write('Texto sin espacios:', processed_text)

# También podríamos mostrar un DataFrame como ejemplo
df = pd.DataFrame({
    'Original Text': [user_input],
    'Processed Text': [processed_text]
})

st.write(df)
