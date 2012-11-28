from distutils.core import setup

setup(
    name='Watson',
    version='0.1dev',
    packages=['watson',],
    license='LICENSE.txt',
    long_description=open('README.md').read(),
    install_requires=[
        "Twisted >= 12.2.0",
        "pinder==1.0.1",
        "wokkel == 0.7.0",
    ],
)