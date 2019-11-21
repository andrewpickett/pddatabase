import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pddatabase",
    version="0.0.1",
    author="Andrew J. Pickett",
    author_email="picketta@gmail.com",
    description="Simple package containing basic database classes/code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andrewpickett/pddatabase",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
