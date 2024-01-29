import numpy as np
import matplotlib.pyplot as plt

def bessel_filter(N, wc, fs, filter_type='lowpass'):
    """
    Design a Bessel filter.

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
        p = np.roots([1, 0, 0, 0, 0, 0, 0, 0, 0, 1])  # 10th order Bessel polynomial roots
        b, a = bessel_transform(p, wc, fs)

    elif filter_type == 'highpass':
        p = np.roots([1, 0, 0, 0, 0, 0, 0, 0, 0, 1])  # 10th order Bessel polynomial roots
        p_hp = -p
        b, a = bessel_transform(p_hp, wc, fs)

    elif filter_type == 'bandpass':
        p = np.roots([1, 0, 0, 0, 0, 0, 0, 0, 0, 1])  # 10th order Bessel polynomial roots
        p_bp = np.exp(1j * np.pi * np.array([1, 3, 5, 7, 9]) / 10)
        b, a = bessel_transform(p * p_bp, wc, fs)

    elif filter_type == 'bandstop':
        p = np.roots([1, 0, 0, 0, 0, 0, 0, 0, 0, 1])  # 10th order Bessel polynomial roots
        p_bs = np.exp(1j * np.pi * np.array([0, 2, 4, 6, 8]) / 10)
        b, a = bessel_transform(p * p_bs, wc, fs)

    return b, a

def bessel_transform(poles, wc, fs):
    """
    Transform Bessel poles to filter coefficients.

    Parameters:
    - poles (numpy.ndarray): Poles of the Bessel filter.
    - wc (float): Cutoff frequency (Hz).
    - fs (float): Sampling frequency (Hz).

    Returns:
    - b (numpy.ndarray): Numerator coefficients of the filter.
    - a (numpy.ndarray): Denominator coefficients of the filter.
    """
    N = len(poles) - 1
    b = np.zeros(N + 1)
    a = np.zeros(N + 1)

    for k in range(N + 1):
        for i in range(k + 1):
            b[k] += np.math.comb(k, i) * wc**(k - i) * poles[i]

    for i in range(N + 1):
        a[i] = wc**i

    b *= fs**N / np.math.factorial(N)
    a *= fs**N / np.math.factorial(N)

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
    plt.title("Bessel Filter Frequency Response")
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Magnitude")
    plt.grid()
    plt.show()
