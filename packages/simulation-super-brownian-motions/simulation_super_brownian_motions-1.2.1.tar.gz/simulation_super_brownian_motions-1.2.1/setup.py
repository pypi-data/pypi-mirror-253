from setuptools import setup, find_packages

setup(
    name='simulation_super_brownian_motions',
    version='1.2.1',
    packages=find_packages(),
    description='This is a package for simulating super Brownian motions.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Le Chen',
    author_email='chenle02@gmail.com',
    url='https://github.com/chenle02/Simulation_Super_Brownian_Motions',
    install_requires=[
        # Any dependencies your package needs, e.g.,
        'numpy',
        'matplotlib',
    ],
    classifiers=[
        # Choose your license as you wish
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'SuperBm=simulation_super_brownian_motions.super_bm_simulation:main',
        ],
    },
)
