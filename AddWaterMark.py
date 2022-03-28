import cv2
import numpy as np
from moviepy.editor import *

inputVideoPath = "testVideo"
outputVideoPath = inputVideoPath + "_marked"
watermark = cv2.imread('watermark.jpg')

# img=cv2.imread("Lenna.jpg")
# print(img.shape)

def process_frame(input_img):

    resized_watermark = cv2.resize(watermark, dsize=(input_img.shape[1],input_img.shape[0]), interpolation=cv2.INTER_NEAREST)
    binary_watermark = resized_watermark >> 7
    output_img = input_img & 0xFE | binary_watermark
    return output_img

if __name__ == '__main__':
    clip = VideoFileClip(inputVideoPath+".mp4")
    transfer_clip = clip.fl_image(process_frame, apply_to=None)
    transfer_clip.write_videofile(outputVideoPath+".mp4", audio=False)


# # 提取音频
# def from_video_get_video():
#     video = VideoFileClip(videoPath)
#     audio = video.audio
#     audioName = videoPpath.split('.', 1)[0] + ".mp3"
#     audio.write_audiofile(audioName)
#     return audioName

# # 添加音频
# def add_audio(video_need_audio):
#     videoWithAudio = VideoFileClip(videoPath)
#     video = VideoFileClip(video_need_audio)
#     audio = videoWithAudio.audio
#     videoclip = video.set_audio(audio)
#     videoName = video_need_audio.split('.', 1)[0] + "_out.mp4"
#     videoclip.write_videofile(videoName)

# if __name__ == '__main__':
#     add_audio('testVideo.mp4')

# # 读取图像，将水印缩放至目标图像大小，并二值化
# ori_img = cv2.imread('Lenna.jpg')
# watermark = cv2.imread('watermark.jpg')
# resized_watermark = cv2.resize(watermark, ori_img.shape[:2], 
# interpolation=cv2.INTER_NEAREST) #既然是二值图像，使用最近邻方式来拉伸比较合适
# binary_watermark = resized_watermark >> 7

# # 嵌入水印并保存结果
# output_img = ori_img & 0xFE | binary_watermark
# cv2.imwrite('Lenna_with_watermark.png', output_img)

# # 提取水印
# img_with_watermark = cv2.imread('Lenna_with_watermark.png')
# extracted_watermark = ((img_with_watermark & 0x01) * 255)
# cv2.imwrite('extracted_watermark.jpg', extracted_watermark)