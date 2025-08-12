from gtts import gTTS
import os

# Read text from file safely
try:
    with open("abc.txt", "r", encoding="utf-8") as f:
        text = f.read().strip()

    if not text:
        raise ValueError("The file is empty.")

    # Convert text to speech
    speech = gTTS(text=text, lang='en', slow=False)
    speech.save("voice.mp3")

    # Play the audio
    os.system("afplay voice.mp3")  # Mac
    # os.system("mpg321 voice.mp3")  # Linux

except FileNotFoundError:
    print("Error: abc.txt file not found.")
except Exception as e:
    print(f"Error: {e}")
