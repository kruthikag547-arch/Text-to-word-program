from gtts import gTTS
import os

text = "Hello, I am kruthika and I am learning Python programming. This is a text-to-speech conversion example using gTTS library."

tts = gTTS(text=text, lang="en")
tts.save("output.mp3")
print("Audio file created successfully!")

# Show where the file was saved
print("File location:", os.path.abspath("output.mp3"))
