import numpy as np
import matplotlib.pyplot as plt

def chebyshev_filter(N, rp, wc, fs, filter_type='lowpass'):
    """
    Design a Chebyshev filter.

    Parameters:
    - N (int): Filter order.
    - rp (float): Passband ripple (dB).
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
        epsilon = np.sqrt(10**(rp / 10) - 1)
        omega_c = np.tan(np.pi * wc / fs)
        k = np.arange(1, N + 1)
        p_real = -np.sin(((2 * k - 1) * np.pi) / (2 * N))
        p_imag = np.sin((k * np.pi) / (2 * N))
        poles = epsilon * (p_real + 1j * p_imag)

        a[0] = 1
        b[0] = epsilon**2 + 1
        for i in range(1, N + 1):
            a[i] = -2 * np.real(poles[i - 1])
            b[i] = epsilon**2 - 2 * epsilon * np.real(poles[i - 1]) + 1

    elif filter_type == 'highpass':
        epsilon = np.sqrt(10**(rp / 10) - 1)
        omega_c = np.tan(np.pi * wc / fs)
        k = np.arange(1, N + 1)
        p_real = -np.sin(((2 * k - 1) * np.pi) / (2 * N))
        p_imag = np.sin((k * np.pi) / (2 * N))
        poles = epsilon * (p_real + 1j * p_imag)

        a[0] = epsilon**2 + 1
        b[0] = 1
        for i in range(1, N + 1):
            a[i] = -2 * np.real(poles[i - 1])
            b[i] = epsilon**2 - 2 * epsilon * np.real(poles[i - 1]) + 1

    elif filter_type == 'bandpass':
        epsilon = np.sqrt(10**(rp / 10) - 1)
        omega_c = np.tan(np.pi * wc[1] / fs) - np.tan(np.pi * wc[0] / fs)
        k = np.arange(1, N + 1)
        p_real = -np.sin(((2 * k - 1) * np.pi) / (2 * N))
        p_imag = np.sin((k * np.pi) / (2 * N))
        poles = epsilon * (p_real + 1j * p_imag)

        a[0] = 1
        b[0] = epsilon**2 + 1
        for i in range(1, N + 1):
            a[i] = -2 * np.real(poles[i - 1])
            b[i] = epsilon**2 - 2 * epsilon * np.real(poles[i - 1]) + 1

    elif filter_type == 'bandstop':
        epsilon = np.sqrt(10**(rp / 10) - 1)
        omega_c = np.tan(np.pi * wc[1] / fs) - np.tan(np.pi * wc[0] / fs)
        k = np.arange(1, N + 1)
        p_real = -np.sin(((2 * k - 1) * np.pi) / (2 * N))
        p_imag = np.sin((k * np.pi) / (2 * N))
        poles = epsilon * (p_real + 1j * p_imag)

        a[0] = epsilon**2 + 1
        b[0] = 1
        for i in range(1, N + 1):
            a[i] = -2 * np.real(poles[i - 1])
            b[i] = epsilon**2 - 2 * epsilon * np.real(poles[i - 1]) + 1

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
    plt.title("Chebyshev Filter Frequency Response")
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Magnitude")
    plt.grid()
    plt.show()