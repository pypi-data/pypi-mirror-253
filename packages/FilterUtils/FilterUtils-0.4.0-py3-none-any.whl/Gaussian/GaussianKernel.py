import numpy as np

def gaussian_kernel_2d(size, sigma):
    """
    Generates a 2D Gaussian kernel.

    Parameters:
    - size (int): Size of the kernel (odd number).
    - sigma (float): Standard deviation of the Gaussian distribution.

    Returns:
    - numpy.ndarray: 2D Gaussian kernel normalized to have a sum of 1.
    """
    x, y = np.meshgrid(np.arange(-size // 2 + 1, size // 2 + 1),
                       np.arange(-size // 2 + 1, size // 2 + 1))
    kernel = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    return kernel / np.sum(kernel)

def gaussian_kernel_3d(size, sigma):
    """
    Generates a 3D Gaussian kernel.

    Parameters:
    - size (int): Size of the kernel (odd number).
    - sigma (float): Standard deviation of the Gaussian distribution.

    Returns:
    - numpy.ndarray: 3D Gaussian kernel normalized to have a sum of 1.
    """
    kernel = np.fromfunction(
        lambda x, y, z: (1/((2*np.pi)**1.5 * sigma**3)) * 
                        np.exp(-((x-(size-1)//2)**2 + (y-(size-1)//2)**2 + (z-(size-1)//2)**2) / (2*sigma**2)),
        (size, size, size)
    )
    return kernel / np.sum(kernel)
