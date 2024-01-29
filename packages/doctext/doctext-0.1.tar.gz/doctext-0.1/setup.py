# your_library_name/setup.py
from setuptools import setup, find_packages

setup(
    name='doctext',
    version='0.1',
    packages=find_packages(),
    license='MIT',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/luckfamousa/doctext',
    author='Felix Nensa',
    author_email='felix.nensa@gmail.com'
)
