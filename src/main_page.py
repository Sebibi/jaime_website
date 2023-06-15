import streamlit as st
import os
from PIL import Image
from src.face_detection import build_face_recognition


def build_main_page():
    st.set_page_config(layout="wide")
    os.environ['OPENAI_API_KEY'] = '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'

    st.header("`Turtle and Bear `")

    is_love = st.checkbox("Do you love me")

    if is_love:
        turtle_bear_image = Image.open('data/turtle_and_bear.jpeg')
        st.image(turtle_bear_image)










