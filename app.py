import streamlit as st
import spacy
from spacy import displacy
from io import StringIO

# Carga del modelo entrenado
@st.cache_resource
def load_model():
    return spacy.load('model-last')

nlp = load_model()

# Título de la aplicación
st.title('📝 Detección Automática de Términos con spaCy')
st.write('Sube un archivo de texto o ingresa un texto manualmente para detectar términos automáticamente usando el modelo entrenado.')

# Entrada de texto
uploaded_file = st.file_uploader("Subir archivo .txt", type=["txt"])
user_text = st.text_area("O ingresa un texto manualmente", height=200)

if uploaded_file is not None:
    # Leer el archivo subido
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    text = stringio.read()
elif user_text:
    text = user_text
else:
    text = None

if text:
    # Procesar el texto con el modelo entrenado
    doc = nlp(text)

    # Mostrar resultados en la interfaz
    st.subheader('📌 Términos Detectados')
    for ent in doc.ents:
        st.write(f"- {ent.text} ({ent.label_})")

    # Mostrar texto resaltado
    st.subheader('📄 Texto Resaltado')
    html = displacy.render(doc, style="ent", jupyter=False)
    st.write(html, unsafe_allow_html=True)
