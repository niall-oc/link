import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="link-game", # Replace with your own username
    version="0.0.1",
    author="Niall O'connor",
    author_email="nyull@yaho.com",
    description="A simple text adventure game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/niall-oc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)