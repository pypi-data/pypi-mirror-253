# setup.py
from setuptools import setup, find_packages

setup(
    name='topsis-shreya-102116042',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'topsis = topsis.topsis:main',
        ],
    },
    author='Shreya Sharma',
    description='TOPSIS analysis package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Shreya2876/topsis-package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        # Add more classifiers as needed
    ],
)
