from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name = 'typergame',
    packages = find_packages(),
    version = '0.3.0',
    description = 'A library to easily set up typergames.',
    author = 'drooler',
    long_description = long_description,
    long_description_content_type='text/markdown'
)

