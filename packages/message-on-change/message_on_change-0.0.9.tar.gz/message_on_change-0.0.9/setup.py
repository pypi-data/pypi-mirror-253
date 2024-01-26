from setuptools import setup, find_packages
from pathlib import Path

VERSION = '0.0.9'
DESCRIPTION = 'message_on_change'
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    entry_points={
        'console_scripts': [
            'message-on-change = message_on_change.guicontroll:main',
            'message-on-change-cli = message_on_change.cli:__main__'
        ],
    },

    name="message_on_change",
    version=VERSION,
    author="Rūdolfs Driķis",
    author_email="drikisr@gmail.com",
    description=DESCRIPTION,
    #long_description=LONG_DESCRIPTION,
    long_description = long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['requests', 'playsound', 'pyside6'],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['python', 'message_on_change', 'pyside6'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        ]
)
