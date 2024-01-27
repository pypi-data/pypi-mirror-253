from setuptools import setup, find_packages
import os

# Utility function to read the README file with specified encoding
def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8') as f:
        return f.read()

setup(
    name="Wallpaper_Group_Symmetry_Dataset",
    version="0.1.1",
    author="Yichen Guo, Joshua Agar",
    author_email="yig319@lehigh.edu, jca92@drexel.edu",
    description="A Python toolkit for generating and analyzing symmetry datasets, based on the mathematical symmetry principle of wallpaper groups.",
    license="MIT",
    keywords="symmetry, wallpaper group, dataset generation",
    url="https://pypi.org/project/Wallpaper-Group-Symmetry-Dataset/",
    packages=find_packages(),
    long_description=read('README.md'),  # Ensure 'README.md' is correctly named and located
    long_description_content_type='text/markdown',  # Specify markdown for long description content type
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    # other parameters as needed
)
