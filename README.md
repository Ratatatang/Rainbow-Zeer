# Rainbow-Zeer

This repo holds the code and instructions for the Rainbow Zeer fortune telling machine.

This is an Eagle scout project by Zander McLane who is working on their eagle project in 2023.

## Prereqs

- Python3
    - install everything in requirements.txt with *** pip install -r requirements.txt ***
- Install mp3 player with *** sudo apt-get install mpg321"

## Audio files
We didn't want the device to rely on an internet connection so we couldn't use gtts as originally intended.  Instead we pre-created all of the MP3 files based on forutunes.txt.  To do this we wrote the script build-mp3s.py which uses AWS Polly for its text to speech engine.  This takes all of the fortunes from fortunes.txt and converts them to MP3s.  We also used polly to create some standard audio files like the intro and some error messages.  

If you want to add additional fortunes, you can delete all of the audio files in audio and then add your new fortunes to fortunes.txt.  Then run the build-mp3s.py script.  You will need to have your AWS cli configured so that boto3 will work with polly.


## References
https://learn.adafruit.com/press-your-button-for-raspberry-pi/assembly
https://learn.adafruit.com/mini-thermal-receipt-printer/circuitpython

## Fortune Contributions by:
- ChatGPT
- SarahJean Meyer
- Marcy Epst
