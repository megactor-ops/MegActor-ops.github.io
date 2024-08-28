import argparse
from tqdm import tqdm
import numpy as np
import os

from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip, ImageSequenceClip
import imageio

if __name__ == '__main__':
    # Read list of videos.
    import glob
    
    # remove video 516*2:516*2+512
    
    video_paths = glob.glob('./*mp4')
    for video_path in tqdm(video_paths):
        video = VideoFileClip(video_path)
        audio = video.audio
        reader = imageio.get_reader(video_path)
        fps = reader.get_meta_data()['fps']
        frames = []
        for frame in reader:
            frame = np.concatenate((frame[:, :516*2], frame[:, 516*3:]), axis=1) # remove control
            frames.append(frame)
        
        # name = video_path.split('/')[-1]
        save_path = video_path
        video = ImageSequenceClip(frames, fps=fps)
        video_with_audio = video.set_audio(audio)
        video_with_audio.write_videofile(save_path, codec='libx264')
    