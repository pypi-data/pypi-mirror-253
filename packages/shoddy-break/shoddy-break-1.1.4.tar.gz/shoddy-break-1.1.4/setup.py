from setuptools import setup, find_packages

setup(
    name='shoddy-break',
    version='1.1.4',
    package_dir={'':'pygame_line_art'},
    packages=find_packages(where='pygame_line_art'),
    install_requires=[
        'pygame',
    ],
    author='FrostDream',
    author_email='frostdream3k@gmail.com',
    description='A pygame based art animation library',
    url='https://github.com/frost-dream/pygame-arts',
)
