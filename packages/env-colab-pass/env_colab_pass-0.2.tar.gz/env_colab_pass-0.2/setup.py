from setuptools import setup, find_packages

# Read the contents of your README file
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='env_colab_pass',
    version='0.2',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=[],
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
