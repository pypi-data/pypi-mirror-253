from setuptools import setup, find_packages
from pathlib import Path

VERSION = '0.0.7'
DESCRIPTION = 'TOPSIS Implementation'
this_directory = Path(__file__).parent
print(this_directory)
LONG_DESCRIPTION = (this_directory/'readme.md').read_text()

# Setting up
setup(
    name="Topsis-Joyy-102117024",
    version=VERSION,
    author="Joyy Goswami",
    author_email="joyy14102002@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description = LONG_DESCRIPTION,
    packages=find_packages(),
    package_data={'':['docs/*.md']},
    install_requires=['pandas', 'numpy'],
    keywords=['topsis', 'decision-analysis', 'similarity','decision-making','multi-criteria-decision'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)