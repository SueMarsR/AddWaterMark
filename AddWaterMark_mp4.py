import cv2
import os
import numpy as np
from moviepy.editor import *

# inputVideoPath = "testVideo.mp4"
# outputVideoPath = "marked_"+inputVideoPath
watermark = cv2.imread('watermark.jpg')
inputPath = os.listdir("./input")
outputPath = os.listdir("./output")


# img=cv2.imread("Lenna.jpg")
# print(img.shape)

def process_frame(input_img):
    resized_watermark = cv2.resize(watermark, dsize=(input_img.shape[1],input_img.shape[0]), interpolation=cv2.INTER_NEAREST)
    binary_watermark = resized_watermark >> 7
    output_img = input_img & 0xFE | binary_watermark
    return output_img

def get_marked(input_img):
    extracted_watermark = ((input_img & 0x01) * 255)
    return extracted_watermark

def check_not_exist(outputVideoPath):
    for i in range(0,len(outputPath)):
        if outputVideoPath == outputPath[i]:
            return False
    return True

    
if __name__ == '__main__':

    for i in range(0,len(inputPath)) : 
        inputVideoPath = "./input/" + inputPath[i]
        outputVideoPath = "./output/" + inputPath[i].split(".", -1)[0] + ".mp4"
        print(inputVideoPath)
        print(outputVideoPath)
        # if check_not_exist(inputPath[i]):

        clip = VideoFileClip(inputVideoPath)
        transfer_clip = clip.fl_image(process_frame, apply_to=None)
        transfer_clip.write_videofile(outputVideoPath, audio=True, codec="libx264", bitrate="12000k")

