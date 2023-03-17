import streamlit as st
from PIL import Image

st.header("Image Color converter App")

with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera", label_visibility="hidden")

if camera_image:
    with Image.open(camera_image) as img:
        grey_img = img.convert(mode="L")

    st.image(grey_img)

uploaded_image = st.file_uploader("Upload your own image")

if uploaded_image:
    with Image.open(uploaded_image) as img2:
        grey_img2 = img2.convert(mode="L")
    st.image(grey_img2)
    