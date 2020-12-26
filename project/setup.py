import setuptools
import re

with open("README.md", "r") as fh:
    long_description = fh.read()

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('marksman/__init__.py', 'r').read(),
    re.M).group(1)


setuptools.setup(
    name="marksman",
    version=version,
    author="Aahnik Daw",
    author_email="meet.aahnik@gmail.com",
    description="CLI Tool to manage marks of students efficiently.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aahnik/cbse-xii-cs-proj/tree/main/project",
    packages=setuptools.find_packages(),
    install_requires=['matplotlib',
                      'PyQt5',
                      'Markdown',
                      'rich',
                      'python-dotenv'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': ['marksman=marksman.cli:main', 'mm=marksman.cli:main'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    license='MIT License',
    keywords=['sql', 'database', 'crud', 'marks management',
              'cms', 'data management', 'cli', 'utility', 'tool'],
)
