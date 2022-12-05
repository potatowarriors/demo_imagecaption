import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import base64

st.title("Demo to auto image captioning")
st.set_page_config(layout="wide", page_title="Image Background Remover")

st.write("## Make caption automatically")
st.write(
    ":dog: Try uploading an image to watch the background magically removed. Full quality images can be downloaded from the sidebar. This code is open source and available [here](https://github.com/tyler-simons/BackgroundRemoval) on GitHub. Special thanks to the [rembg library](https://github.com/danielgatis/rembg) :grin:"
)
st.sidebar.write("## Upload and download")

my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
