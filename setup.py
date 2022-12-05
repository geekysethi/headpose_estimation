from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
VERSION = '0.0.2'
DESCRIPTION = 'Head pose estimation module'

# Setting up
setup(
    name="headpose_detection",
    version=VERSION,
    author="Ashish Sethi",
    author_email="<ashish18024@iiitd.ac.in>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['efficientnet'],
    keywords=['python', 'image', 'face detection', 'headpose estimation', 'machine learning', 'computer vision'],
    include_package_data=True,


)