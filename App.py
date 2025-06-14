import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os
from gtts import gTTS
from moviepy.editor import *

st.set_page_config(page_title="SosoVideo - AI Script to Video", layout="centered")

st.title("🎬 SosoVideo - Turn Your Script into a Video")

script = st.text_area("Enter your script here", height=200)

if st.button("Generate Video"):
    if not script.strip():
        st.error("Please enter a script.")
    else:
        with st.spinner("Generating video..."):

            # Generate image with text
            img = Image.new('RGB', (720, 480), color=(255, 255, 255))
            d = ImageDraw.Draw(img)
            font = ImageFont.load_default()
            d.text((50, 200), script[:500], fill=(0, 0, 0), font=font)

            image_path = "frame.png"
            img.save(image_path)

            # Generate voice
            tts = gTTS(text=script, lang='en')
            audio_path = "audio.mp3"
            tts.save(audio_path)

            # Create video
            image_clip = ImageClip(image_path).set_duration(10)
            audio_clip = AudioFileClip(audio_path).subclip(0, 10)
            video = image_clip.set_audio(audio_clip)
            video_path = "output.mp4"
            video.write_videofile(video_path, fps=24)

        st.success("Video generated!")
        st.video(video_path)
