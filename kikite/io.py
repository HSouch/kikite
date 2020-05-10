""" Input and output processing """

# from pathlib import Path
import warnings
import librosa


def read_file(filename):
    """
    Reads in a given input file and converts it to workable data.
    :param filename:
    :return:
    """

    # I'm saving pydub formas as an array for future proofing.
    audioread_formats = ["mp3"]
    soundfile_formats = ["flac", "ogg", "wma"]

    extension = filename.split(".")[len(filename.split(".")) - 1]

    # if extension in audioread_formats:
    #     y, sr = librosa.load()

    y, sr = librosa.load(filename)

    print(type(y), type(sr))

    return None
