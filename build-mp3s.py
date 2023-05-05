import boto3
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir

polly = boto3.client('polly')

def create_mp3(text, filename):
    try:
        # Request speech synthesis
        response = polly.synthesize_speech(Engine='neural', LanguageCode='en-US', VoiceId='Salli', OutputFormat='mp3', Text=text)
    except (BotoCoreError, ClientError) as error:
        # The service returned an error, exit gracefully
        print(error)
        sys.exit(-1)

    # Access the audio stream from the response
    if "AudioStream" in response:
        # Note: Closing the stream is important because the service throttles on the
        # number of parallel connections. Here we are using contextlib.closing to
        # ensure the close method of the stream object will be called automatically
        # at the end of the with statement's scope.
            with closing(response["AudioStream"]) as stream:
                output = f"./audio/{filename}"

                try:
                    # Open a file for writing the output as a binary stream
                        with open(output, "wb") as file:
                            file.write(stream.read())
                except IOError as error:
                    # Could not write to file, exit gracefully
                    print(error)
                    sys.exit(-1)

    else:
        # The response didn't contain audio data, exit gracefully
        print("Could not stream audio")
        sys.exit(-1)   

# read in the file
with open('fortunes.txt', 'r') as f:
    fortunes = f.readlines()

for fortune in fortunes:
    print(fortune)
    create_mp3(fortune, fortune.replace(' ', '_').replace('\n', '').replace('.', '') + '.mp3')
