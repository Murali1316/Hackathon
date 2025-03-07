**Personalized Voice Cloning using XTTS v2
This project enables personalized voice cloning using XTTS v2. It takes a short voice sample and synthesizes speech in the same voice using any given text.**

🚀 Features
Upload a short voice sample.
Enter text to synthesize speech in the same voice.
Runs locally without external APIs.
Uses Flask backend and HTML/JavaScript frontend.
📂 Project Structure
php
Copy code
├── app.py                  # Flask backend
├── templates/
│   ├── index.html          # Frontend UI
├── static/
│   ├── styles.css          # (Optional) CSS styles
├── uploads/                # Folder for uploaded audio files
├── output/                 # Folder for synthesized audio
├── requirements.txt        # Python dependencies
├── README.md               # This file
⚙️ Setup Instructions
1️⃣ Install Dependencies
Ensure Python 3.9+ is installed, then run:

bash
Copy code
pip install -r requirements.txt
2️⃣ Download XTTS v2 Model
bash
Copy code
python -c "from TTS.api import TTS; TTS('tts_models/multilingual/multi-dataset/xtts_v2')"
3️⃣ Run Flask Server
bash
Copy code
python app.py
The app will run at http://127.0.0.1:5000/.

🛠️ API Endpoints
📌 Upload Audio
bash
Copy code
POST /upload
Body: Form-data, key = input_file, value = .wav file
Response: { "message": "File uploaded successfully", "filepath": "path/to/file.wav" }
📌 Generate Speech
bash
Copy code
POST /synthesize
Body (JSON):
json
Copy code
{
  "text": "Hello, this is a cloned voice.",
  "speaker_wav": "path/to/uploaded.wav"
}
Response: Returns generated .wav file.
🌟 Demo
Upload a voice sample.
Enter text.
Click "Generate" to hear the cloned voice!
💡 Notes
For GPU acceleration, install CUDA and use gpu=True in TTS().
Make sure Flask is running before sending API requests.
🛠️ Future Improvements
UI enhancements
Support for multiple languages
Deploying to cloud
