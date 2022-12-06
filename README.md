# Auto captioning web application
* 이번 proejct는 Streamlit (https://streamlit.io/) API를 활용하여 자동 주석 생성 web application을 개발해봤습니다.
* 주석 생성을 위해 사용한 Deep learning model은 CLIP(https://github.com/openai/CLIP)과 GPT-2(https://github.com/openai/gpt-2)를 기반으로 하여 COCO(https://cocodataset.org/#home)에 학습시킨 CLIP Prefix Caption(https://github.com/rmokady/CLIP_prefix_caption) model을 활용했습니다.


# Application의 사용법.
![alt text](https://github.com/[potatowarriors]/[demo_imagecaption]/blob/[main]/image.jpg?raw=true) \
1. 좌측 side bar에 이미지를 업로드 한다. (가능한 확장자 : jpg, png, jpeg)
2. 자동으로 upload한 image와 주석이 표기된다.