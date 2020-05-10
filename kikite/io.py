""" Input and output processing """

from pathlib import Path
# import librosa
# import pydub


def read_file(filename):
    """
    Reads in a given input file and converts it to workable data.
    :param filename:
    :return:
    """

    extension = filename.split(".")[len(filename.split(".")) - 1]

    print(extension)

    return None
