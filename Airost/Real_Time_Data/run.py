import os
import time
from typing_extensions import Annotated
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import numpy as np
import xml.etree.ElementTree as ET

import torch
from torch.utils.data import dataloader
from model.malexnet import mAlexNet
from model.alexnet import AlexNet

from torchvision import transforms

import matplotlib.pyplot as plt

from firebase import update_db

def extract_info_from_xml(xml_file):
    root = ET.parse(xml_file).getroot()

    # Initialise the info dict 
    info_list = []
    info_dict = {}

    for elem in root:
        info_dict['id'] = elem.attrib['id']
        info_dict['occupied'] = elem.attrib['occupied']

        for sub in elem:
            if sub.tag == "rotatedRect":
                for subElem in sub:
                    if subElem.tag == "center":
                        info_dict['centerX'] = subElem.attrib['x']
                        info_dict['centerY'] = subElem.attrib['y']
                    elif subElem.tag == "size":
                        info_dict['sizeW'] = subElem.attrib['w']
                        info_dict['sizeH'] = subElem.attrib['h']
                    elif subElem.tag == "angle":
                        info_dict['angle'] = subElem.attrib['d']
            # elif sub.tag == "contour":
            else:
                i = 0                                                                                  
                for subElem in sub:    
                    info_dict[f'pointX[{i}]'] = subElem.attrib['x']
                    info_dict[f'pointY[{i}]'] = subElem.attrib['y']
                    i += 1

        list = [
                int(info_dict['id']), int(info_dict['occupied']), 
                int(info_dict['pointX[0]']), int(info_dict['pointY[0]']),
                int(info_dict['pointX[1]']), int(info_dict['pointY[1]']),
                int(info_dict['pointX[2]']), int(info_dict['pointY[2]']),
                int(info_dict['pointX[3]']), int(info_dict['pointY[3]']),
                int(info_dict['sizeW']), int(info_dict['sizeH']),
            ]
        info_list.append(list)

    return info_list

PATH = 'model1.pth'

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.RandomResizedCrop(224),
    transforms.ToTensor(),  # normalize to [0, 1]
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
]) 


def load_model(img, square):
    model = mAlexNet().to(device)
    model.load_state_dict(torch.load(PATH))

    model.eval()
    img1 = img.crop(square)
    # newIm.show()
    img_t = transform(img1)
    batch_t = torch.unsqueeze(img_t, 0)
    out = model(batch_t)

    _, indices = torch.max(out, 1)
    percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100

    print(percentage[indices[0]].item())
    print(indices)

    if percentage[indices[0]].item() < 55:
        return 3

    return indices[0].numpy()

def crop_image(img, polygon):
    # read image as RGB and add alpha (transparency)
    im = img.convert("RGBA")

    # convert to numpy (for convenience)
    imArray = np.asarray(im)

    # create mask
    # polygon = [(444,203),(623,243),(691,177),(581,26),(482,42)]
    maskIm = Image.new('L', (imArray.shape[1], imArray.shape[0]), 0)
    ImageDraw.Draw(maskIm).polygon(polygon, outline=1, fill=1)
    mask = np.array(maskIm)

    # assemble new image (uint8: 0-255)
    newImArray = np.empty(imArray.shape,dtype='uint8')

    # colors (three first columns, RGB)
    newImArray[:,:,:3] = imArray[:,:,:3]

    # transparency (4th column)
    newImArray[:,:,3] = mask*255

    # back to Image from numpy
    newIm = Image.fromarray(newImArray, "RGBA")
    newIm.save("out.png")

ROOT_PATH = "Image Path"

xml_file = [os.path.join(ROOT_PATH, x) for x in os.listdir(ROOT_PATH) if x[-3:] == "xml"]

for annotate_file in xml_file:
    image_file = annotate_file.replace(".xml", ".jpg")

    img = Image.open(image_file)
    img1 = Image.open(image_file)
    img_draw = ImageDraw.Draw(img)  

    info = extract_info_from_xml(annotate_file)
    for x in info:
        top_left_x = min([x[2],x[4],x[6],x[8]]) + 10
        top_left_y = min([x[3],x[5],x[7],x[9]]) + 10
        bot_right_x = max([x[2],x[4],x[6],x[8]]) - 10
        bot_right_y = max([x[3],x[5],x[7],x[9]]) - 10

        shape = [(top_left_x, top_left_y), (bot_right_x, bot_right_y)]

        occupied = load_model(img, (top_left_x, top_left_y, bot_right_x, bot_right_y))

        img_draw.text((x[2], x[3]), f"{x[0]}", fill ="red")
        if occupied == 1:
            img_draw.rectangle(shape, outline ="red")
            update_db(x[0], 1)
        elif occupied == 0:
            img_draw.rectangle(shape, outline ="green")
            update_db(x[0], 0)
        else:
            img_draw.rectangle(shape, outline ="blue")

    img.show()
    img.close()
    time.sleep(10)
