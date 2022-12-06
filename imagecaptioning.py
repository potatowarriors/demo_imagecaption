import streamlit as st
from make_caption import makecap
from PIL import Image

st.title("2022 F/W Web Python Term Project")

st.write(
    "Project 개요 : 이미지에 자동으로 주석을 만들어주는 Deep learning model을 사용하여 web application으로 개발했습니다. 이번 project에 사용한 model은 [CLIP](https://github.com/openai/CLIP) model을 기반으로 하여 COCO dataset에 training한 [CLIP prefix caption](https://github.com/rmokady/CLIP_prefix_caption) model을 활용했습니다."
)

st.write("## 이미지 자동 주석 생성기")
st.write("")
st.write("##### 좌측 사이드바에 이미지를 업로드 하여 자동으로 주석을 생성해보세요.")
st.sidebar.write("## 업로드")

def uploader_callback():
    print('Uploaded new file')

my_upload = st.sidebar.file_uploader("주석을 생성할 이미지를 업로드 하세요", type=["png", "jpg", "jpeg"], on_change=uploader_callback)

if my_upload is not None:
    image = Image.open(my_upload)
    caption = makecap(my_upload)
    st.image(image)
    st.write('###### Caption : ',caption)
    