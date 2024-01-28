from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.1'
DESCRIPTION = 'A basic database structure, like sqlite3.'
LONG_DESCRIPTION = 'A package that allows you to store strings and stuff in a secure database file'

# Setting up
setup(
    name="steelbase",
    version=VERSION,
    author="SteelDev",
    author_email="<stupidnaive8@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['database', 'db', 'sqlite', 'pydb', 'pydatabase', 'steelbase', 'steeldatabase'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)