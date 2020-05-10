""" Main file for data processing """

import kikite as kk
import argparse

test_filename = "test_data/test.mp3"

kk.read_file(test_filename)


input_filename = ""


def read_arguments():
    """
    Read in and process command-line arguments using argparse.
    :return:
    """
    global input_filename

    # Set up parser and process arguments
    parser = argparse.ArgumentParser(description="Automatic processing of chords from audio files.",
                                     epilog="This is very much a WIP.")
    parser.add_argument("input_filename", type=str,
                        help="The required name of the file for processing.")

    args = parser.parse_args()

    # Affix arguments to global variables here
    input_filename = args.input_filename

    return args


args = read_arguments()
