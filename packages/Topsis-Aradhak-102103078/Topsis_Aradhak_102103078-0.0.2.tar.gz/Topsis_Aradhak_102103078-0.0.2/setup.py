from setuptools import setup
import setuptools

with open("README.md", "r") as f:
    description = f.read()

setup(
    name='Topsis_Aradhak_102103078',
    version='0.0.2',
    description='Python package for implementing TOPSIS technique.',
    author= 'Aradhak Kandhari',
#    url = 'https://github.com/Spidy20/PyMusic_Player',
    long_description=description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=['Topsis'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=['Topsis_Aradhak_102103078'],
    package_dir={'':'src'}
#    install_requires = [
#        'mutagen',
#        'pygame',
#        'ttkthemes'
#    ]
)
