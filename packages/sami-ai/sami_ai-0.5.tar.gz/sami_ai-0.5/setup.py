from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='sami_ai',
    version='0.5',
    packages=['sami_ai'],
    install_requires=['requests'],
    author="SamiSoft - Yemen",
    url="https://github.com/mr-sami-x/sami_ai",
    description="This library is an advanced artificial intelligence to help with advanced and fast software and solutions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
