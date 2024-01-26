import os
from setuptools import setup

requirements = [
    "pika==1.3.2",
    "threadpool>=1.3.2",
]

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='sca-core',
    version='0.0.6',
    packages=[
            "sca_core",
    ],
    license='BSD License',
    description='sca core',
    install_requires=requirements,
    long_description_content_type="text/markdown",
    url='',
    author='lijun0927',
    author_email='lijun@njis.ac.cn',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
)