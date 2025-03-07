from flask import Flask, request, jsonify, send_file
import os
from TTS.api import TTS

app = Flask(__name__)

# Corrected directories
UPLOAD_FOLDER = r"D:\Murali\uploads"
OUTPUT_FOLDER = r"D:\Murali\output"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Load TTS Model
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

@app.route("/upload", methods=["POST"])
def upload_audio():
    if "input_file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["input_file"]
    filename = os.path.join(UPLOAD_FOLDER, "input_file.wav")  # Save with fixed name
    file.save(filename)

    return jsonify({"message": "File uploaded successfully", "filepath": filename})

@app.route("/synthesize", methods=["POST"])
def synthesize_voice():
    data = request.json
    text = data.get("text", "").strip()
    speaker_wav = os.path.join(UPLOAD_FOLDER, "input_file.wav")  # Use uploaded file

    if not text:
        return jsonify({"error": "Text is required"}), 400

    if not os.path.exists(speaker_wav):
        return jsonify({"error": "Speaker audio file not found"}), 400

    output_wav = os.path.join(OUTPUT_FOLDER, "cloned_voice.wav")
    
    # Run text-to-speech conversion
    tts.tts_to_file(text=text, speaker_wav=speaker_wav, language="en", file_path=output_wav)

    return send_file(output_wav, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
