# ePDFpy
ePDFpy is a standalone tool for reduced electron pair distribution function (ePDF) analysis. Users can do ePDF analysis with the diffraction images obtained by transmission electron microscope (TEM), and use the outputs to deduce the atomic structures.

This software is Python-based software with an interactive graphical user interface (GUI) environment built with PyQt5. Currently, built with the python3.8 version but confirmed that still compatible with python3.10.

# Installation
For the convenience, it is recommended to use Anaconda (www.anaconda.com/download) or Miniconda ( https://docs.conda.io/en/latest/miniconda.html) to set up a virtual environment. All dependencies can easily installed by using 'environment.yaml' file in the conda terminal:

First, users must install pre-requiste libralies, which are listed in below:

- numpy >= 1.22.4
- scipy >= 1.9.1
- opencv (cv2) >= 4.6.0
- pandas >= 1.4.4
- pyqt5 >= 5.15.7
- pyqtgraph >= 0.12.4
- hyperspy >= 1.7.1
- mrcfile >= 1.4.2
- pyqtdarktheme == 2.1.0

Users can install all dependencies manually using pip install or conda install. 
```
pip install -r requirements.txt
```
or
```
conda env create --file environment.yaml
```

It is recommended to install ePDFpy via PyPI or Anaconda distribution. Users can establish the virtual environment (), then use following command line to install.

```
pip install epdfpy
```
or
```
conda install epdfpy
```

## Using source code

If users want to install ePDFpy directly from the source code, download the source code, and moved into the directory path. Using terminal type:
```
python setup.py install
```

## ePDFpy GUI package
For those who are not familiar with Python, users can simply download executable files for each OS (Windows, Mac, Linux), which are compiled with PyInstaller.
Simply open the executable file:
- Windows: ePDFpy.exe
- Mac: ePDFpy.app



# Running GUI

After installation, users can open ePDFpy simply typing command line in the terminal:
```
epdfpy
```
which will automatically opens the GUI script (run_ui.py) in source folder.

Those who are not accustomed to Python, just open executable files from distributed package.

# Example
![example](https://github.com/GWlab-SKKU/ePDFpy/assets/59153513/aa1f59c5-0daa-4276-81f4-d48a829b3b56)


# License

GNU GPLv3

**ePDFpy** is open-source software distributed under a GPLv3 license.
It is free to use, alter, or build on, provided that any work derived from **ePDFpy** is also kept free and open under a GPLv3 license.
