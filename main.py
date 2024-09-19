from flask import Flask, render_template, request, send_file
from solver import get_trad_sentence
from config import llm2
import torch
from TTS.api import TTS
import os
from pydub import AudioSegment
import tempfile

# Init TTS model
device = "cuda" if torch.cuda.is_available() else "cpu"
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

app = Flask(__name__)

# Créer le dossier "output" s'il n'existe pas
if not os.path.exists("output"):
    os.makedirs("output")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Récupérer l'audio uploadé par l'utilisateur
        if "audio" not in request.files:
            return "Aucun fichier audio fourni", 400
        
        audio_file = request.files["audio"]
        
        # Sauvegarder l'audio temporairement
        audio_path = os.path.join("output", "input_audio.wav")
        audio_file.save(audio_path)

        # Appeler la fonction pour traduire la phrase en anglais (ici on suppose qu'on a l'audio transcrit en français)
        transcribed_text = "Salut comment vas-tu ?"  # Placeholder pour l'extraction du texte
        translated_text = get_trad_sentence(transcribed_text)

        # Générer le nouvel audio avec la voix clonée en anglais
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_audio_file:
            temp_audio_path = temp_audio_file.name
            wav = tts.tts(text=translated_text, speaker_wav=audio_path, language="en")

            # Sauvegarder l'audio généré dans le fichier temporaire
            temp_audio_file.write(wav)
        
        # Utiliser AudioSegment pour s'assurer que le fichier est lisible
        audio = AudioSegment.from_wav(temp_audio_path)
        output_audio_path = os.path.join("output", "output_audio.wav")
        audio.export(output_audio_path, format="wav")

        return send_file(output_audio_path, as_attachment=True)

    return '''
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Clone et Traduction de Voix</title>
      </head>
      <body>
        <div style="text-align:center;">
          <h1>Clone et Traduction de Voix</h1>
          <form method="POST" enctype="multipart/form-data">
            <input type="file" name="audio" accept="audio/*">
            <br><br>
            <input type="submit" value="Envoyer">
          </form>
        </div>
      </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(debug=True)
