import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = ["pynput>=1.6.8"]

setuptools.setup(
    name="keyboard",  # Replace with your own username
    version="0.0.12",
    author="Erfan Nariman",
    author_email="erfan.nariman@briccanalytics.nl",
    description="Module to do random keystroaks or mouse movements "
                "to prevent your laptop going to sleep",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/erfannariman/keyboard",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "keyboard=main.keyboard:run"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
