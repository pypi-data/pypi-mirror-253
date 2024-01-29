from setuptools import setup, find_packages

with open('./README.md',mode='r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='japantime',
    version='1.1.9',
    packages=find_packages(),
    author='inu',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
