import os
import json
import re
import time

SUFFIX = 'm4s'

# 读取json文件
def readJson(fileName):
    f = open(fileName, encoding='utf-8')
    setting = json.load(f)
    title = setting['title']
    return title

# 获取文件列表
def getFileList(file_dir):
    # 定义三个列表
    Title = []
    VideoPath = []
    AudioPath = []
    # 遍历文件目录
    for root, dirs, files in os.walk(file_dir):
        if ('.videoInfo' in files):
            Tname = str(root) + '.videoInfo'
            Tname = readJson(Tname)
            Title.append(Tname)
        # if ('video.m4s' in files and 'audio.m4s' in files):
        #     Vpath = str(root) + '\\video.m4s'
        #     Apath = str(root) + '\\audio.m4s'
        #     VideoPath.append(Vpath)
        #     AudioPath.append(Apath)
        # if ('0.blv' in files):
        #     Title.pop()
        for eachfile in files:
            if eachfile.split(".")[-1] == SUFFIX:
                VideoPath.append(os.path.join(file_dir, eachfile))
    return [Title, VideoPath]


# 输出mp4文件
def getMP4(title, video_path):
    # 生成输出目录
    if not os.path.exists("./output"):
        os.mkdir("./output")
    # 循环生成MP4文件
    for i in title:
        # 规范文件名
        cop = re.compile("[^\u4e00-\u9fa5^a-z^A-Z^0-9]")  # 匹配不是中文、大小写、数字的其他字符
        reName = i
        reName = cop.sub('', reName)  # 将标题中匹配到的字符替换成空字符
        # 开始生成MP4文件
        if not os.path.exists("./output/" + reName + ".mp4"):
            os.system(
                "ffmpeg -i " + ' -i '.join(video_path) + " -codec copy ./output/" + reName + ".mp4")
            print("正在合成...")
            print("标题：" + i)
            print("视频源：" + video_path[title.index(i)])
            time.sleep(1)
