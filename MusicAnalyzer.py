import os
import sys
import shutil
from pathlib import Path

from pydub import AudioSegment
import wave
import audioop
import ffmpeg

from scipy.io import wavfile
import numpy as np
import scipy

import matplotlib.pyplot as plt

# import librosa
# import librosa.display


class MusicAnalyzer:
    def list_files(self, directories):  # John

        directory = directories[0]
        workspace = directories[1]

        if os.path.exists(workspace):
            shutil.rmtree(workspace)

        files = []

        for _, _, file_list in os.walk(directory):
            for file in file_list:
                if file.endswith(".wav") or file.endswith(".mp3"):
                    files.append(file)

        return files

    def copy_files_to_workspace(self, files, directories):  # John

        directory = directories[0]
        workspace = directories[1]

        if os.path.exists(workspace):
            shutil.rmtree(workspace)

        os.mkdir(workspace)

        for file in files:
            shutil.copyfile(directory + "/" + file, workspace + "/" + file)

    def crossfade(self, directories):  # Sailon

        directory = directories[0]
        workspace = directories[1]

        if os.path.exists(workspace):
            shutil.rmtree(workspace)

        files = []

        for _, _, file_list in os.walk(directory):
            for file in file_list:
                if file.endswith(".wav") or file.endswith(".mp3"):
                    files.append(file)

        directory = directories[0]
        playlist = []

        for file in files:
            if file.endswith(".wav"):
                playlist.append(AudioSegment.from_wav(directory + "/" + file))
            if file.endswith(".mp3"):
                playlist.append(AudioSegment.from_mp3(directory + "/" + file))

        combined = playlist[0]
        for song in playlist[1:]:
            combined = combined.append(song, crossfade=5000)

        combined.export(directory + "/Crossfaded_Playlist" + ".wav", format="wav")

    def convert_mp3_to_wav(self, file_list, directories):  # Sailon

        workspace = directories[1]
        converted_files = []

        for file in file_list:

            if file.endswith(".mp3"):

                sound = AudioSegment.from_mp3(workspace + "/" + file)
                sound.export(
                    workspace + "/" + file.replace(".mp3", "") + ".wav", format="wav"
                )
                os.remove(workspace + "/" + file)

            converted_files.append(file.replace(".mp3", ".wav"))

        return converted_files

    def rename_files(self, files, directories):  # John

        i = 1
        workspace = directories[1]
        renamed_files = []

        for file in files:

            if file != (str(i) + ".wav"):
                os.rename(workspace + "/" + file, workspace + "/" + str(i) + ".wav")
                renamed_files.append(str(i) + ".wav")

            else:
                renamed_files.append(file)

            i += 1

        return renamed_files

    def convert_stereo_to_mono(self, file_list, directories):  # Sailon
        workspace = directories[1]

        for file in file_list:

            fileX = wave.open(workspace + "/" + file, "r")
            if fileX.getnchannels() != 1:

                frames, audiodata = wavfile.read(workspace + "/" + file)
                audiodata = audiodata.astype(float)

                newaudiodata = []
                d = (audiodata[:, 0] + audiodata[:, 1]) / 2
                newaudiodata.append(d)
                a = np.array(newaudiodata, dtype="int16")

                wavfile.write(workspace + "/" + file, frames, a.T)

    #    def convert_stereo_to_mono(self,file_list,directories):

    #        workspace = directories[1]

    #        for file in file_list:
    #            fileX = wave.open(workspace + "/" + file, 'r')
    #            if fileX.getnchannels != 1:
    #                converted_file = AudioSegment.from_wav(workspace + "/" + file)
    #                converted_file = converted_file.set_channels(1)
    #                converted_file.export(workspace + "/" + file, format="wav")

    def audio_details(self, file, directories):  # John

        workspace = directories[1]

        audio_file = wave.open(workspace + "/" + file, "r")
        channels_num = audio_file.getnchannels()
        samp_width = audio_file.getsampwidth()
        frame_rate = audio_file.getframerate()
        frames_num = audio_file.getnframes()
        audio_file.close()

        details = [channels_num, samp_width, frame_rate, frames_num]
        return details

    def plot_graph(self, files, file, directories, position):  # John

        workspace = directories[1]

        spf = wave.open(workspace + "/" + file, "r")

        signal = spf.readframes(-1)
        signal = np.fromstring(signal, "Int16")

        plt.figure(1)
        plt.xlabel("Tempo")
        plt.ylabel("Amplitude")
        plt.title("Gráfico do arquivo: " + files[position] + "...")
        plt.rcParams["figure.figsize"] = (11, 7)
        plt.plot(signal)
        # plt.show()


"""
    def show_spectrogram(self, files, file, directories, position): #Sailon

        workspace = directories[1]

        x , sr = librosa.load(workspace + "/" + file)

        X = librosa.stft(x)
        Xdb = librosa.amplitude_to_db(abs(X))
        #plt.figure(figsize=(14, 5))
        plt.figure(2)
        librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
        plt.colorbar()
        plt.title("Espectograma do arquivo: " + files[position] + "...")
        #plt.show()

    def show_center_of_mass(self, files, file, directories, position): #Sailon

        workspace = directories[1]

        x , sr = librosa.load(workspace + "/" + file)


        spectral_centroids = librosa.feature.spectral_centroid(x, sr=sr)[0]
        spectral_centroids.shape

        frames = range(len(spectral_centroids))
        t = librosa.frames_to_time(frames)

        plt.figure(3)

        ax1 = plt.subplot(2, 1, 1)
        librosa.display.waveplot(x, sr=sr, alpha=0.5)
        plt.title("Gráfico do arquivo: " + files[position] + "...")

        plt.subplot(2, 1, 2, sharex=ax1)
        plt.plot(t, spectral_centroids, color='r')
        plt.title("Centroide do arquivo: " + files[position] + "...")

        plt.tight_layout()

        #plt.show()

    def show_notes(self, files, file, directories, position): #Sailon
        
        workspace = directories[1]
        x , sr = librosa.load(workspace + "/" + file, duration=15)
        
        chromagram = librosa.feature.chroma_stft(x, sr=sr, hop_length=512)
        
        plt.figure(4)
        
        librosa.display.specshow(chromagram, x_axis='time', y_axis='chroma', hop_length=512, cmap='coolwarm')
        
        plt.title('Gráfico do áudio x')
        plt.xlabel('Tempo (s)')
        plt.ylabel('Notas')
        
        plt.show()
"""
