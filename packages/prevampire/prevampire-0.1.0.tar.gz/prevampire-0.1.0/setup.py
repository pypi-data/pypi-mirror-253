from setuptools import setup, find_packages

setup(
    name='prevampire',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'scikit-image',
        'vampire',
        'skan',
        'pandas',
        'scipy', 
    ],
    entry_points={
        'console_scripts': [
            'prevampire-cli = prevampire.cli:main',
        ],
    },
    author='Mia Onodera',
    author_email='mconodera@gmail.com',
    description='Supplementary Package to Apply to existing VAMPIRE package pipeline.',
    url='https://github.com/onoderamia/prevampire',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
