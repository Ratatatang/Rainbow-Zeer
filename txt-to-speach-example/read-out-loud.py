text = 'Let me look into your future'

from gtts import gTTS
import os

tts = gTTS(text, lang='en', tld='ie')
with open('intro.mp3', 'wb') as f:
    tts.write_to_fp(f)

os.system('mplayer intro.mp3')
