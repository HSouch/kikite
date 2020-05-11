""" Methods for processing music into frequencies """

from numpy import array
from numpy.fft import rfft


def get_frequencies(sample, sample_rate=22050, threshold=0.3, uniqueness_threshold=5):
    """
    Obtains frequencies
    :param sample: The input sound file
    :param sample_rate:
    :param threshold:
    :param uniqueness_threshold:
    :return:
    """

    sample_length = sample, sample_rate
    # Calculate the Fourier transform of the sample and normalize it
    sample_fft = abs(rfft(sample))
    fft_max = max(sample_fft)

    sample_fft /= fft_max

    good_coefficients = []

    # Obtain all coefficients above the defined threshold
    # todo make this loop faster? Surely there's a numpy method for it
    for n in range(0, len(sample_fft)):
        if sample_fft[n] > threshold:
            good_coefficients.append(n)

    # Convert Fourier coefficients to frequencies in Hertz, and remove those less than 20Hz.
    good_freqs = array(good_coefficients) / sample_length
    good_freqs = good_freqs[good_freqs > 20]

    # Gather all unique elements, (so no duplicates are considered)
    unique_frequencies = []
    for i in range(0, len(good_freqs)):
        unique = True
        for j in range(0, len(unique_frequencies)):
            if abs(good_freqs[i] - unique_frequencies[j]) < uniqueness_threshold:
                unique = False
                break
        if unique:
            unique_frequencies.append(good_freqs[i])

    unique_frequencies = array(unique_frequencies)

    print(unique_frequencies)

    return unique_frequencies


def process_audio_file(audio, precision=None):
    """ Runs rolling window through audio to get chords at different times. """
    return None
