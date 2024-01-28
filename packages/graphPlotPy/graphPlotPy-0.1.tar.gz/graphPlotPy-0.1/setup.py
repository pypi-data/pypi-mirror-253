from setuptools import setup, find_packages

setup(
    name='graphPlotPy',
    version='0.1',
    packages=find_packages(),
    description='A Python package for plotting graphs',
    install_requires=[
        "colorama>=0.4.6",
        "colorlog>=6.8.0",
        "colormap>=1.0.6",
        "contourpy>=1.2.0",
        "cycler>=0.12.1",
        "easydev>=0.12.1",
        "fonttools>=4.47.2",
        "kiwisolver>=1.4.5",
        "matplotlib>=3.8.2",
        "mpmath>=1.3.0",
        "numpy>=1.26.3",
        "packaging>=23.2",
        "pexpect>=4.9.0",
        "pillow>=10.2.0",
        "ptyprocess>=0.7.0",
        "pyparsing>=3.1.1",
        # "dateutil>=2.8.2",
        "setuptools>=69.0.3",
        "six>=1.16.0",
        "sympy>=1.12",
    ]
)

