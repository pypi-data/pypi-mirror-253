import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plastexshowmore",
    version="0.0.1",
    author="Patrick Massot",
    description="Show more buttons for plasTeX.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    package_data={'plastexdepgraph': ['static/*', 'Packages/*']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent"],
    python_requires='>=3.7',
    install_requires=['plasTeX>=3.0']
)
