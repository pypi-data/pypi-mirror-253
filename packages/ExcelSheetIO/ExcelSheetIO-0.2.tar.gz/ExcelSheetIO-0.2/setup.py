import codecs
from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='ExcelSheetIO',
    version='0.2',
    author="Soumyajit Pan",
    author_email="soumyajitpan29@gmail.com",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    description='A Python package for efficient Excel sheet operations. Enables easy read/write functionality, data manipulation, and workflow automation. Ideal for handling both small and large datasets. Get started with ExcelSheetIO for a simplified data processing experience.',
    keywords=['excel', 'excelreader', 'excelwriter', 'python', 'excel reader and writer', 'read excel data using python', 'write data in excel using python', 'excelsheetio'],
    install_requires=[
        'attrs==23.2.0',
        'certifi==2023.11.17',
        'cffi==1.16.0',
        'et-xmlfile==1.1.0',
        'exceptiongroup==1.2.0',
        'h11==0.14.0',
        'idna==3.6',
        'natsort==8.4.0',
        'openpyxl==3.1.2',
        'outcome==1.3.0.post0',
        'pycparser==2.21',
        'PySocks==1.7.1',
        'robotframework==7.0',
        'robotframework-pabot==2.17.0',
        'robotframework-pythonlibcore==4.3.0',
        'robotframework-seleniumlibrary==6.2.0',
        'robotframework-stacktrace==0.4.1',
        'selenium==4.16.0',
        'sniffio==1.3.0',
        'sortedcontainers==2.4.0',
        'trio==0.24.0',
        'trio-websocket==0.11.1',
        'urllib3==2.1.0',
        'wsproto==1.2.0',
    ],
)
