from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    readme_content = f.read()

setup(
    name='fastotp-sdk',
    version='1.0.0',
    packages=find_packages(),
    install_requires=['requests', 'enum34'],
    author='Ibrahim Oluwapeluwa',
    author_email='ipeluwa@gmail.com',
    description='A Python SDK for the FastOTP service',
    long_description=readme_content,
    long_description_content_type='text/markdown',
    url='https://github.com/ipeluwa/fastotp-sdk',
)


