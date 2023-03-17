import streamlit as st
from converter import convert_image
st.header("Image Color converter App")

with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera", label_visibility="hidden")

if camera_image:
    grey_camera_image = convert_image(camera_image)

    st.image(grey_camera_image)

uploaded_image = st.file_uploader("Upload your own image")

if uploaded_image:
    grey_uploaded_image = convert_image(uploaded_image)

    st.image(grey_uploaded_image)
