from setuptools import setup, find_packages

setup(
    name='FilterUtils',
    version='2.0.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [],
    },
    author='Jarvis',
    author_email='Jarvis@ldsb.com',
    description='A Python library for various filters',
    long_description='A Python library providing implementations of Bessel, Butterworth, Cauer, Chebyshev, and Gaussian filters.',
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
