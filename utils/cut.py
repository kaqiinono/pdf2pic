# coding=gbk

from moviepy.editor import VideoFileClip
import os

def cut(path, des):
    files = os.listdir(path)
    file_index = 1
    for one_file in files:
        name_arr = one_file.split(".")
        if name_arr[-1] == 'mp4':
            my_clip = VideoFileClip(path + one_file)
            print(one_file + ' 时长：', end='')
            print(my_clip.duration)
            subclip = my_clip.subclip(7.0167, -7.93)
            file_name = des + name_arr[-2] + ".mp4"
            subclip.write_videofile(file_name)
            subclip.audio.write_audiofile(des + name_arr[-2] + ".mp3")
            my_clip.close()
        file_index += 1
