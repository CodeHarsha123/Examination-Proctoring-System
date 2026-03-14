import pyaudio
import numpy as np
from proctoring.logger import log_event

def detect_noise():
    CHUNK = 1024
    RATE = 44100
    THRESHOLD = 2000

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    while True:
        data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
        volume = np.linalg.norm(data)
        if volume > THRESHOLD:
            log_event("Suspicious noise detected")
