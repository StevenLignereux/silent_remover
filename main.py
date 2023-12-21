from wave_file_manager import *
import matplotlib.pyplot as plt


def normalize_samples(samples, max_value):
    max_sample = max(abs(max(samples)), abs(min(samples)))
    f = max_value / max_sample

    return [s * f for s in samples]


# Lecture du fichier wav et réccupération des samples
wav_samples = wave_file_read_samples("test1.wav")

if wav_samples == None:
    print("ERREUR: Aucun sample à la lecture du fichier wav")
    exit(0)

# normaliser les samples
wav_samples_norm = normalize_samples(wav_samples, 1000)

# Matplotlib
plt.plot(wav_samples_norm)
plt.show()
