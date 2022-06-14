import pyaudio
from tqdm import tqdm

def record_and_play(record_seconds):
    ## audio format setting
    auformat = pyaudio.paInt16
    channels = 1
    rate = 44100
    chunk = 1024
    
    p = pyaudio.PyAudio()
    recording_stream = p.open(format=auformat, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)
    playing_stream = p.open(format=auformat, channels=channels, rate=rate, output=True, frames_per_buffer=chunk)

    for i in tqdm(range(0, int(rate / chunk * record_seconds))):
        data = recording_stream.read(1024)
        playing_stream.write(data)

    recording_stream.stop_stream()
    playing_stream.stop_stream()
    recording_stream.close()
    playing_stream.close()
    p.terminate()

## record and play 10 seconds

record_and_play(10)
