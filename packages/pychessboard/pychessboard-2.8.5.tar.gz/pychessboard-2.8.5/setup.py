from setuptools import setup, find_packages

setup(
    name='pychessboard',
    version='2.8.5',
    packages=find_packages(),
    install_requires=[
        'pygame'
    ],
    author='James gonzalez',
    author_email='nadernmds@gmail.com',
    description='a chessboard game',
    long_description=open('README').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/nadernmds/pychessboard',
)
