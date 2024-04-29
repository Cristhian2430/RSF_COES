import streamlit as st
import pandas as pd
import datetime

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

# Mostrar el texto procesado
st.write('Texto sin espacios:', processed_text)

# También podríamos mostrar un DataFrame como ejemplo
df = pd.DataFrame({
    'Original Text': [user_input],
    'Processed Text': [processed_text]
})

st.write(df)
