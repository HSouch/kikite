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

    extension = filename.split(".")[len(filename.split(".")) - 1]

    y, sr = librosa.load(filename)

    

    return None
