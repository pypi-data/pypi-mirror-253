from setuptools import setup, find_packages

setup(
    name='my_pyrttov',
    version='0.1',
    description='Ma bibliothèque Python Rttov pour ubuntu 22.04',
    author='Yoanne DIDRY',
    author_email='yoanne.didry@list.lu',
    packages=find_packages(include=['my_rttov', 'my_rttov.*']),
    install_requires=[
    ],
)
