from setuptools import setup, find_packages
from pathlib import Path

VERSION = '0.0.4'
DESCRIPTION = 'Implementing TOPSIS'
this_directory = Path(__file__).parent
print(this_directory)
LONG_DESCRIPTION = (this_directory/'readme.md').read_text()

# Setting up
setup(
    name="Topsis-Aaditya-102117021",
    version=VERSION,
    author="intrinsicvardhan (Aaditya Vardhan)",
    author_email="intrinsicvardhan@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description = LONG_DESCRIPTION,
    packages=find_packages(),
    package_data={'':['docs/*.md']},
    install_requires=['pandas', 'numpy'],
    keywords=['topsis', 'decision-analysis', 'similarity'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)