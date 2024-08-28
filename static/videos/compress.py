from moviepy.editor import VideoFileClip

def compress_video(input_path, output_path, target_resolution=(1280, 720), target_bitrate="500k"):
    # Load the video
    video = VideoFileClip(input_path)

    # Resize the video
    video_resized = video.resize(height=target_resolution[1])

    # Write the compressed video
    video_resized.write_videofile(
        output_path, 
        bitrate=target_bitrate,
        # codec='libx264',  # Codec for good compression
        audio_codec='aac'  # Audio codec
    )

# Example usage
compress_video("2024_08_22.mp4", "output_video.mp4", target_resolution=(2802 * 3 // 3, 1080 * 3 // 3), target_bitrate="1600k")