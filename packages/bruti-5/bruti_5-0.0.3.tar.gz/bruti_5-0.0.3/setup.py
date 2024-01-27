#[project.urls]
#Homepage = "https://github.com/asif-cods/tools-code/"

from setuptools import setup

VERSION = '0.0.3'
DESCRIPTION = 'A Tool to Brute-Force login page username and password'
LONG_DESCRIPTION = 'This is a tool deveoloped by security researcher to perform bruteforce.'

try:
	with open("README.md", "r", encoding="utf-8") as fh:
		long_description = fh.read()
except TypeError:
	with open("README.md","r") as fh:
		long_description = fh.read()

setup(
    name="bruti_5",
    version=VERSION,
    author="Asif_H4CKER",
    author_email="<rajm34022@gmail.com>",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        'console_scripts': [
            'bruti_5 = bruti_5.bruti_5:main',
        ],
    },
    install_requires=['requests'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

