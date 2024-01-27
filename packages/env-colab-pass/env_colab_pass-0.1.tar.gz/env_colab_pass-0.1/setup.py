from setuptools import setup, find_packages

setup(
    name='env_colab_pass',
    version='0.1',
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=[
        # List your package dependencies here
        'os',
        'getpass',
    ],
    extras_require= {
        'google-colab': ['google-colab']
    }, 
    # Other metadata
    author='Bakulkumar Kakadiya',
    author_email='bakul.kumar@gmail.com',
    description='Python library that check for key value in env and colab userdata. if not found then asks for it using getpass',
    license='Apache License Version 2.0',
    url='https://github.com/bkakadiya/env-colab-pass',
)
