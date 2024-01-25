from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'hello'
LONG_DESCRIPTION = 'A package to perform hello message'

# Setting up
setup(
    name="Hello123",
    version=VERSION,
    author="Soumyajit Pan",
    author_email="soumyajitpan29@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['excel', 'excelreader', 'excelwriter', 'python', 'excel reader and writer', 'read excel data using python', 'write data in excel using python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)