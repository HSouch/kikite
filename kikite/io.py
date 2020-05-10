""" Input and output processing """

import time
import warnings
import librosa


def read_file(filename, verbose=False):
    """
    Reads in a given input file and converts it to workable data.
    :param filename:
    :return:
    """
    warnings.filterwarnings("ignore")  # We don't care if librosa has to default to audiostream (I think)

    y, sr, t_start = None, None, time.time()

    try:
        extension = filename.split(".")[len(filename.split(".")) - 1]
        y, sr = librosa.load(filename)
    except FileNotFoundError:
        print("Error." + filename + " does not exist.")
        exit(1)

    warnings.filterwarnings("default")

    if verbose:
        print(filename + " successfully loaded. Time elapsed: " + str(time.time() - t_start)[:6] + " seconds.")

    return y, sr


def new_test():
    return None