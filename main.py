from gtts import gTTS
import os

mytext = 'hi, this is an example of converting text to audio'
audio = gTTS(text=mytext, lang='en', slow=False)

audio.save('audio/example.mp3')
os.system('open audio/example.mp3')