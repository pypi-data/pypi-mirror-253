import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='endemic',
    version='0.1.19',
    description='Endemic misc class',
    long_description=README,
    long_description_content_type="text/markdown",
    url="",
    author="Dima Denisov",
    author_email='python@endemic.ru',
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    include_package_data=True,
    install_requires=['pymysql', 'fluent-logger'],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),  # Required
)
