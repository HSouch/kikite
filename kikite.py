""" Main file for data processing """

import kikite as kk
import argparse


input_filename = ""


def read_arguments():
    """
    Read in and process command-line arguments using argparse.
    :return: arguments
    """

    global input_filename

    # Set up parser and process arguments
    parser = argparse.ArgumentParser(description="Automatic processing of chords from audio files.",
                                     epilog="This is very much a WIP.")
    parser.add_argument("input_filename", type=str,
                        help="The required name of the file for processing.")

    cl_args = parser.parse_args()

    # Affix arguments to global variables here
    input_filename = cl_args.input_filename

    return cl_args


args = read_arguments()
