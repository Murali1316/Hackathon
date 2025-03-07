from TTS.api import TTS

# Load the pretrained XTTS v2 model (Runs Locally)
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)

def clone_voice(text, voice_sample):
    output_file = "cloned_voice.wav"
    tts.tts_to_file(text=text, speaker_wav=voice_sample, language="en", file_path=output_file)
    return output_file

# Example Usage
text = "Hello! This is my cloned voice speaking."
voice_sample = "your_voice_sample.wav"  # Replace with your sample file

output = clone_voice(text, voice_sample)
print("Generated voice file:", output)
