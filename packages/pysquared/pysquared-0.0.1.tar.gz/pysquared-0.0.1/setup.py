import pathlib
from setuptools import setup, find_packages

PACKAGE_NAME = 'pysquared'

CWD = pathlib.Path(__file__).parent

README_PATH = (CWD / "README.md").read_text()

setup(
    name=PACKAGE_NAME,
    version="0.0.1",
    description="Pipeline automation framework for Python",
    long_description=README_PATH,
    long_description_content_type="text/markdown",
    author="Nikolai Krivoshchapov",
    author_email="nikolai.krivoshchapov@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        'numpy',
        'networkx',
        'pandas',
        'textwrap3',
        'prompt-toolkit',
        'openpyxl',
        'xlcalculator',
    ]
)
