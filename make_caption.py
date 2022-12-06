#@title Imports

import clip
import os
from torch import nn
import numpy as np
import torch
import torch.nn.functional as nnf
import sys
from typing import Tuple, List, Union, Optional
from transformers import GPT2Tokenizer, GPT2LMHeadModel, AdamW, get_linear_schedule_with_warmup
from tqdm import tqdm, trange
import skimage.io as io
import PIL.Image
from utils import generate2
from modeling import ClipCaptionModel
   


#@title CLIP model + GPT2 tokenizer
def makecap(input_image):
    device = "cpu"
    clip_model, preprocess = clip.load("ViT-B/32", device=device, jit=False, download_root='/data/kide004/repos/web_project/demo_imagecaption/pre-trained')
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    prefix_length = 10

    model = ClipCaptionModel(prefix_length)
    

    model_path = '/data/kide004/repos/web_project/demo_imagecaption/pre-trained/model_weights.pt'
    model.load_state_dict(torch.load(model_path, map_location='cpu'), strict=False) 

    model = model.eval() 
    device =  "cpu"
    model = model.to(device)

    #@title Inference
    use_beam_search = False #@param {type:"boolean"}


    ### inferfence 이제 이게 streamlit안으로 들어갈 예정.
    image = io.imread(input_image)
    pil_image = PIL.Image.fromarray(image)

    image = preprocess(pil_image).unsqueeze(0).to(device)
    with torch.no_grad():
        # if type(model) is ClipCaptionE2E:
        #     prefix_embed = model.forward_image(image)
        # else:
        prefix = clip_model.encode_image(image).to(device, dtype=torch.float32)
        prefix_embed = model.clip_project(prefix).reshape(1, prefix_length, -1)
        
    generated_text_prefix = generate2(model, tokenizer, embed=prefix_embed)
    return generated_text_prefix