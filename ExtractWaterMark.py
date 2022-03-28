import cv2
import os
import numpy as np
from moviepy.editor import *


def get_marked(input_img):
    extracted_watermark = ((input_img & 0x01) * 255)
    return extracted_watermark


if __name__ == '__main__':
    # outputPath = os.listdir("./output")
    # for i in range(0,len(outputPath)) : 
    #     outputVideoPath = "./output/"+outputPath[i]
    #     clip = VideoFileClip(outputVideoPath).subclip(0,3)
    #     frame = clip.get_frame(1)
    #     watermark = get_marked(frame)

    #     if not os.path.exists("./check/"):
    #         os.makedirs("./check/")

    #     cv2.imwrite("./check/watermark_"+str(i)+"_"+outputPath[i].split(".",-1)[0]+".png", watermark)

    outputVideoPath = "./output/《鱼缸》Fish Bowl，郑腾飞,14'28.mp4"
    # print(outputVideoPath.split(".",-1)[1].split("/",-1)[2])
    clip = VideoFileClip(outputVideoPath).subclip(20,30)
    frame = clip.get_frame(26)
    watermark = get_marked(frame)

    if not os.path.exists("./check/"):
        os.makedirs("./check/")

    cv2.imwrite("./check/watermark_"+outputVideoPath.split(".",-1)[1].split("/",-1)[2]+".png", watermark)