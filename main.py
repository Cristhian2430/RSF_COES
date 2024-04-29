import streamlit as st
import pandas as pd
import datetime
import os

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

ruta_trabajo = st.text_input('Ingrese la ruta de trabajo donde desea guardar el archivo CSV:', '')

# Entrada para el nombre del archivo
nombre_archivo = st.text_input('Ingrese el nombre del archivo CSV:', 'datos.csv')

# Crear un DataFrame de ejemplo
data = {
    'Columna1': [1, 2, 3],
    'Columna2': [4, 5, 6]
}
df = pd.DataFrame(data)

def guardar_csv(ruta, nombre):
    # Construir la ruta completa del archivo
    ruta_completa = os.path.join(ruta, nombre)
    # Guardar el DataFrame como CSV
    df.to_csv(ruta_completa, index=False)
    return ruta_completa

if st.button('Guardar CSV'):
    if ruta_trabajo and nombre_archivo:
        # Asegurarse de que la ruta existe
        if not os.path.exists(ruta_trabajo):
            st.error("La ruta especificada no existe. Por favor, ingrese una ruta válida.")
        else:
            ruta_completa = guardar_csv(ruta_trabajo, nombre_archivo)
            st.success(f'Archivo CSV guardado exitosamente en: {ruta_completa}')
    else:
        st.error('Por favor, complete los campos de ruta y nombre del archivo.')
