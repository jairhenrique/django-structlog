from setuptools import setup

import django_structlog

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='django-structlog',
    version=django_structlog.__version__,
    author='Jules Robichaud-Gagnon',
    author_email='j.robichaudg+pypi@gmail.com',
    description='Structured Logging for Django',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/jrobichaud/django-structlog',
    packages=[
        'django_structlog',
    ],
    install_requires=[
        'django>=1.11'
        'structlog',
        'django-ipware',
    ],
    license="MIT",
    classifiers=[
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: PyPy",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)