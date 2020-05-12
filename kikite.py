""" Main file for data processing """

import kikite as kk
import argparse


input_filename = ""
signal_threshold = 0.3


def read_arguments():
    """
    Read in and process command-line arguments using argparse.
    :return: arguments
    """

    global input_filename
    global signal_threshold

    # Set up parser and process arguments
    parser = argparse.ArgumentParser(description="Automatic processing of chords from audio files.",
                                     epilog="This is very much a WIP.")
    parser.add_argument("input_filename", type=str,
                        help="The required name of the file for processing.")
    parser.add_argument("-t", "--threshold", type=float,
                        help="The threshold required to consider a signal in the FFT as an actual note. " +
                             "(Default is 0.3).")

    cl_args = parser.parse_args()

    # Affix arguments to global variables here
    input_filename = cl_args.input_filename

    if cl_args.threshold is not None:
        signal_threshold = cl_args.threshold

    return cl_args


args = read_arguments()

kk.io.read_file(input_filename, verbose=True)

