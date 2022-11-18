import moviepy.editor as mp

def extract_audio(videos_file_path):
    my_clip = mp.VideoFileClip(videos_file_path)
    my_clip.audio.write_audiofile(f'{videos_file_path}.mp3')

extract_audio(r'../files/318837459_nb2-1-30080.m4s')