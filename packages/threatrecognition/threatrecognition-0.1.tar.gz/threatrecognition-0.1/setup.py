from setuptools import setup, find_packages

setup(
    name='threatrecognition',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'SpeechRecognition',
        'pyaudio'
    ],
    entry_points={
        'console_scripts': [
            'threat-recognition = threatrecognition.main:main'
        ],
    },
    license='MIT',
    long_description=open('README.md').read(),
)