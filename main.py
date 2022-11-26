import base64
from io import BytesIO
import streamlit as st
import pandas as pd
from PIL import Image
image = Image.open('avatar.jfif')


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.save()
    processed_data = output.getvalue()
    return processed_data

def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    val = to_excel(df)
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="MeusDados.xlsx">Clique em mim para baixar</a>' # decode b'abc' => abc


with st.sidebar:
    st.image(image, caption='DataScience Jr.', width=200)
    st.title("Samuel Alexandre Azevedo Gomes")
    link = '[Linkedin 📚](https://www.linkedin.com/in/samuel-alexandre-56251a145/)'
    st.title(link)

separador = st.text_input('Por gentileza, informe o SEPARADOR')
uploaded_file = st.file_uploader("Subir Arquivo CSV ")

try:
    if uploaded_file is not None :

        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file, sep = separador)
        st.dataframe(dataframe)
        df = dataframe
        with st.spinner('Estamos Preparando seu Download 🛠👷‍'):
            st.markdown(get_table_download_link(df), unsafe_allow_html=True)
            st.success('Sucesso!!!! ')
            st.balloons()


except ValueError:
    if TypeError == 'exceptions must derive from BaseException':
        pass
    else:
        pass