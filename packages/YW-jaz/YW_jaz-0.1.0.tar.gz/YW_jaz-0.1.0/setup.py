from setuptools import setup, find_packages

with open("readme.md", "r") as fh:
    long_description = fh.read()

setup(
    name='YW_jaz',
    version='0.1.0',
    author='Yulun Wu',
    author_email='yulunwu8@gmail.com',
    description='YWs jaz processing tool',
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3'
    ],
    python_requires='>=3.8',
    install_requires=['matplotlib','pandas','numpy']
)











