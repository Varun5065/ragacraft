from audiocraft.models import MusicGen
import streamlit as st 
import torch 
import torchaudio
import os 
import numpy as np
import base64
import openai
import time

# openai.api_key = "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"
# OPENAI_API_KEY = "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"
st.set_page_config(page_icon= "notes", page_title= "AudioCraft")

@st.cache_data
def generate_music_prompt(user_input):
    prompt = f"""There is a new AI called MusicGen which can generate a song given a prompt. 
Generate a text to music prompt as per user chat [OR the choice of user as per chat], include several relevant parameters such as tempo, scale, pitch, rhythm, dynamics, texture, timbre, etc. for an optimized romantic mood. 
Specify suitable alues for each of these features from your knowledge and include in the prompt generated. 
Make it in 50-100 words. 
This prompt is given as a prompt to ai music generator musicgen. Choose mood as per user input.
The following is a description of the user's image: {user_input}
Create a prompt for MusicGen that represents the suer input."""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
            ],
        temperature=0.4,
        max_tokens=400,
        top_p=0.95,
        stop=[
            "console.log(csv);"
        ]
    )
    
    text = response.choices[0].message.content
    return text

def load_model():
    model = MusicGen.get_pretrained('small')
    return model

def generate_music_tensors(description, duration: int):
    """Generates music tensors from a description and duration.

    Args:
        description (str): A description of the music to generate.
        duration (int): The duration of the music in seconds.

    Returns:
        A list of music tensors.
    """
    # Here, I have changed the name of the function to `generate_music_tensors`.
    # I have also added a docstring to describe the function.

    model = load_model()

    model.set_generation_params(
        use_sampling=True,
        top_k=250,
        duration=duration
    )

    output = model.generate(
        descriptions=[description],
        progress=True,
        return_tokens=True
    )

    return output[0]

def save_audio(samples: torch.Tensor):
    """Saves audio from a tensor.

    Args:
        samples (torch.Tensor): A tensor of audio samples.

    Returns:
        The path to the saved audio file.
    """
    # Here, I have changed the name of the function to `save_audio`.

    sample_rate = 32000
    save_path = "audio_output/"
    os.makedirs(save_path, exist_ok=True)

    assert samples.dim() == 2 or samples.dim() == 3

    samples = samples.detach().cpu()
    if samples.dim() == 2:
        samples = samples[None, ...]

    for idx, audio in enumerate(samples):
        audio_path = os.path.join(save_path, f"audio_{idx}.wav")
        torchaudio.save(audio_path, audio, sample_rate)

    return save_path

def get_binary_file_downloader_html(bin_file, file_label='File'):
    """Generates HTML code for downloading a binary file.

    Args:
        bin_file (str): The path to the binary file.
        file_label (str): The label for the download button.

    Returns:
        The HTML code.
    """
    # Here, I have changed the name of the function to `get_binary_file_downloader_html`.

    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href

st.markdown(
    """
    <style>
    .stApp {
        background-color: #C9DFEC;
        color: #ffffff;
    }
    .stTextInput, .stSlider, .stButton {
        background-color: #C9DFEC;
        border: none;
        color: #000000;
    }
    .stTextInput:hover, .stSlider:hover, .stButton:hover {
        background-color: #C9DFEC;
    }
    .stSubheader {
        color: #4CAF50;
    }
    .stText {
        color: #000000;
    }
    .stSlider div[data-baseweb="slider"] {
        background-color: #C9DFEC;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    st.title("Your Musical Desires, Our Creation")
    
    text_area = st.text_area("Enter your description:")
    selected_duration = st.radio("Select time duration (In Seconds)", [5, 10, 15, 20])


    music_prompt = None
    
    if st.button("Create Music Prompt", key="create_music_prompt"):
        if text_area and selected_duration:
            st.subheader("Generated Music Prompt")
            music_prompt = generate_music_prompt(text_area)
            st.write(f'<h7 style="color: black;">{music_prompt}</h7>', unsafe_allow_html=True)

    if st.button("Generate Music", key="generate_music"):
        with st.spinner("Loading..."):
            time.sleep(25)
            music_tensors = generate_music_tensors(music_prompt, selected_duration)
            save_music_file = save_audio(music_tensors)
            audio_filepath = 'audio_output/audio_0.wav'
            audio_file = open(audio_filepath, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes)
            st.markdown(get_binary_file_downloader_html(audio_filepath, 'Audio'), unsafe_allow_html=True)



if __name__ == "__main__":
    main()


    
