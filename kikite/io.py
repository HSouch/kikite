""" Input and output processing """

import time
import warnings
import librosa


def read_file(filename, verbose=False, sample_rate=22050):
    """
    Reads in a given input file and converts it to workable data.
    :param filename:
    :param sample_rate: sample rate when reading in file. Default is 22050 Hz
    :return:
    """
    warnings.filterwarnings("ignore")  # We don't care if librosa has to default to audiostream (I think)

    y, sr, t_start = None, None, time.time()

    try:
        extension = filename.split(".")[len(filename.split(".")) - 1]
        y, sr = librosa.load(filename, sr=sample_rate)
    except FileNotFoundError:
        print("Error." + filename + " does not exist.")
        exit(1)

    warnings.filterwarnings("default")

    if verbose:
        print(filename + " successfully loaded. Time elapsed: " + str(time.time() - t_start)[:6] + " seconds.")
        print("Length of input audio: " + str(len(y) / sample_rate)[:10] + " seconds.")

    return y, sr
