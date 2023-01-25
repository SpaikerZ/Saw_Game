from playsound import playsound
playsound('audio/output.wav')


from gtts import gTTS
import os

hello_my_dear = 'Привет дорогой мой друг'
hello_my_dear_audio = gTTS(text=hello_my_dear, lang='ru', slow=True)
hello_my_dear_audio.save('audio/hello_my_dear(1).mp3')

os.system('open audio/example.mp3')
