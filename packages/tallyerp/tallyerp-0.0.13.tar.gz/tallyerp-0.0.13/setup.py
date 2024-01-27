from setuptools import setup, find_packages
import sys

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

sys.path[0:0] = ['src/tallyerp']


setup(
    name='tallyerp',
    version='0.0.13',
    description='Tally ERP python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='citrisys',
    author_email='dev@citrisys.com',
    url='https://citrisys.com',
    packages=(find_packages(where="src")),
    package_dir={"": "src"},
    requires=['requests', 'loguru', 'xsdata'],
)