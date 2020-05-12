""" Contains all processing of music related stuff from input frequencies """

from numpy import array, sum

# Define keys
key_c = 0
key_c_sharp, key_d_flat = 1, 1
key_d = 2
key_d_sharp, key_e_flat = 3, 3
key_e = 4
key_f = 5
key_f_sharp, key_g_flat = 6, 6
key_g = 7
key_g_sharp, key_a_flat = 8, 8
key_a = 9
key_a_sharp, key_b_flat = 10, 10
key_b = 11


class Note:
    """ Basic class for musical note objects."""
    def __init__(self, key=1):
        self.key = key


def freq_to_note(frequency):
    """ Converts a frequency into a given musical note """
    return None


def determine_key(notes):
    """ Estimates the key from a given set of notes. """
    notes = array(notes)
    c_major = array([1, 3, 5, 6, 8, 10, 12])
    c_minor = array([1, 3, 4, 5, 6, 9, 11])

    for n in range(0, 12):
        root = n
        count_major, count_minor = 0, 0
        for note in notes:
            if note in c_major:
                count_major += 1
            if note in c_minor:
                count_minor += 1

        print(to_letter(root), "\tMajor:", count_major, "\tMinor:", count_minor)

        c_major = (c_major + 1) % 12
        c_minor = (c_minor + 1) % 12

    return None


def to_letter(key: int):
    """ Converts an integer key value back into it's easily readable letter counterpart"""
    def zero():
        return "C"

    def one():
        return "C#"

    def two():
        return "D"

    def three():
        return "D#"

    def four():
        return "E"

    def five():
        return "F"

    def six():
        return "F#"

    def seven():
        return "G"

    def eight():
        return "G#"

    def nine():
        return "A"

    def ten():
        return "A#"

    def eleven():
        return "B"

    options = {0: zero, 1: one, 2: two, 3: three, 4: four, 5: five, 6: six,
               7: seven, 8: eight, 9: nine, 10: ten, 11: eleven}
    letter_key = options[key]()

    return letter_key


determine_key((1, 8, 9))
