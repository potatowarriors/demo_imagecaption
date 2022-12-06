# Auto captioning web application
* 이번 proejct는 Streamlit (https://streamlit.io/) API를 활용하여 자동 주석 생성 web application을 개발해봤습니다.
* 주석 생성을 위해 사용한 Deep learning model은 CLIP(https://github.com/openai/CLIP)과 GPT-2(https://github.com/openai/gpt-2)를 기반으로 하여 COCO(https://cocodataset.org/#home) dataset에 학습시킨 CLIP Prefix Caption(https://github.com/rmokady/CLIP_prefix_caption) model을 활용했습니다.
<br/>
<br/>
<br/>
# Application의 사용법.
<img width="1741" alt="스크린샷 2022-12-06 오후 3 23 37" src="https://user-images.githubusercontent.com/90762128/205839455-6dea50a6-fdbb-42ea-9cbf-9036a365f0eb.png">
<hr>
1. 좌측 side bar에 이미지를 업로드 한다. (가능한 확장자 : jpg, png, jpeg)
<br/>
2. 자동으로 upload한 image와 주석이 표기된다.