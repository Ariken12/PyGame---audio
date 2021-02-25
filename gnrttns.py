from gnrtsmpl import *

freq_array = np.array([261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 10000])

def generate_tones(duration):
    global freq_array
    tones = []
    for freq in freq_array:
        # np.array нужен для преобразования данных под формат 16 бит (dtype=np.int16)
        tone = np.array(generate_sample(freq, duration, 1.0), dtype=np.int16)
        tones.append(tone)
    return tones