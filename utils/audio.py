import moviepy.editor as mp
import os


def extract_audio(videos_file_path):
    my_clip = mp.VideoFileClip(videos_file_path)
    my_clip.audio.write_audiofile(f'{videos_file_path}.mp3')


def extract(videos_file_path, des):
    files = os.listdir(videos_file_path)
    file_index = 1
    for one_file in files:
        name_arr = one_file.split(".")
        if name_arr[-1] == 'mp4':
            print(des + name_arr[-2] + ".mp3")
            my_clip = mp.VideoFileClip(videos_file_path + one_file)
            my_clip.audio.write_audiofile(des + name_arr[-2] + ".mp3")
            # my_clip.close()
        file_index += 1


extract('/Users/songmeinuo/Music/SightWords/', '/Users/songmeinuo/PycharmProjects/pythonProject/mp3/')
