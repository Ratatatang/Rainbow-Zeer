text = 'Your future looks so bright, Ive got to wear shades'

from gtts import gTTS
import os

tts = gTTS(text, lang='en', tld='ie')
with open('test.mp3', 'wb') as f:
    tts.write_to_fp(f)

os.system('mplayer test.mp3')
