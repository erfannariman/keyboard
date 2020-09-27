from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = ["pynput>=1.7.1"]

setup(
    name="keyboard",
    version="0.0.2",
    author="Erfan Nariman",
    author_email="erfannariman@gmail.com",
    description="Module to do random keystroaks or mouse movements "
                "to prevent your laptop going to sleep",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/erfannariman/keyboard",
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "keyboard=src.keyboard:run"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
