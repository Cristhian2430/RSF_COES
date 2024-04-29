import streamlit as st
import pandas as pd
import datetime
import os
import base64
from io import BytesIO

st.set_page_config(page_title   = "RSF", 
                   page_icon    = ":chart:",
                   layout       = "wide")

st.title('Reserva Secundaria de Frecuencia (RSF)')

ruta_trabajo = st.text_input('Ruta de Trabajo:', '')

today = datetime.datetime.now()
next_year = today.year + 1
jan_1 = datetime.date(next_year, 1, 1)
dec_31 = datetime.date(next_year, 12, 31)

d = st.date_input(
    "Select your vacation for next year",
    (jan_1, datetime.date(next_year, 1, 7)),
    jan_1,
    dec_31,
    format="MM.DD.YYYY",
)
d


# También podríamos mostrar un DataFrame como ejemplo
df = pd.DataFrame({
    'Original Text': ["1"],
    'Processed Text': ["2"]
})

st.write(df)

# Título de la aplicación
st.title('Descargar CSV con Streamlit')

# Crear un DataFrame de ejemplo
data = {
    'Columna1': [1, 2, 3],
    'Columna2': [4, 5, 6]
}
df = pd.DataFrame(data)

# Función para convertir el DataFrame a CSV y codificarlo para la descarga
def get_csv_download_link(df):
    # Convertir DataFrame a CSV
    csv = df.to_csv(index=False)
    # Codificar y crear el enlace de descarga
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="datos.csv">Descargar CSV</a>'
    return href

# Botón para descargar el CSV
if st.button('Descargar CSV'):
    st.markdown(get_csv_download_link(df), unsafe_allow_html=True)
