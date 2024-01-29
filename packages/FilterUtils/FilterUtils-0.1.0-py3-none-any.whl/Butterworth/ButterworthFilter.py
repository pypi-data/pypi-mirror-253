import numpy as np
import matplotlib.pyplot as plt

def butterworth_filter(N, wc, fs, filter_type='lowpass'):
    """
    Design a Butterworth filter.

    Parameters:
    - N (int): Filter order.
    - wc (float): Cutoff frequency (Hz).
    - fs (float): Sampling frequency (Hz).
    - filter_type (str): Filter type ('lowpass', 'highpass', 'bandpass', 'bandstop').

    Returns:
    - b (numpy.ndarray): Numerator coefficients of the filter.
    - a (numpy.ndarray): Denominator coefficients of the filter.
    """
    b = np.zeros(N + 1)
    a = np.zeros(N + 1)

    if filter_type == 'lowpass':
        c = np.tan(np.pi * wc / fs)
        a[0] = 1 + np.sqrt(2)*c + c**2
        a[1] = 2 * (c**2 - 1)
        a[2] = 1 - np.sqrt(2)*c + c**2

        b[0] = c**2 / a[0]
        b[1] = 2 * c**2 / a[0]
        b[2] = c**2 / a[0]

    elif filter_type == 'highpass':
        c = np.tan(np.pi * wc / fs)
        a[0] = 1 + np.sqrt(2)*c + c**2
        a[1] = 2 * (c**2 - 1)
        a[2] = 1 - np.sqrt(2)*c + c**2

        b[0] = 1 / a[0]
        b[1] = -2 / a[0]
        b[2] = 1 / a[0]

    elif filter_type == 'bandpass':
        wc2 = 2 * np.pi * wc[1] / fs
        wc1 = 2 * np.pi * wc[0] / fs
        c = np.tan((wc2 - wc1) / 2)
        a[0] = 1 + np.sqrt(2)*c + c**2
        a[1] = 2 * (c**2 - 1)
        a[2] = 1 - np.sqrt(2)*c + c**2

        b[0] = 2 * c / a[0]
        b[1] = 0
        b[2] = -2 * c / a[0]

    elif filter_type == 'bandstop':
        wc2 = 2 * np.pi * wc[1] / fs
        wc1 = 2 * np.pi * wc[0] / fs
        c = np.tan((wc2 - wc1) / 2)
        a[0] = 1 + np.sqrt(2)*c + c**2
        a[1] = 2 * (c**2 - 1)
        a[2] = 1 - np.sqrt(2)*c + c**2

        b[0] = 1 / a[0]
        b[1] = -2 * np.cos((wc2 + wc1) / 2) / a[0]
        b[2] = 1 / a[0]

    return b, a

def plot_filter_response(b, a, fs):
    """
    Plot the frequency response of the filter.

    Parameters:
    - b (numpy.ndarray): Numerator coefficients of the filter.
    - a (numpy.ndarray): Denominator coefficients of the filter.
    - fs (float): Sampling frequency (Hz).
    """
    w, h = freqz(b, a, fs=fs)
    plt.figure()
    plt.plot(0.5 * fs * w / np.pi, np.abs(h), 'b')
    plt.title("Butterworth Filter Frequency Response")
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Magnitude")
    plt.grid()
    plt.show()