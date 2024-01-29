import setuptools

with open("./app/README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name = "PhasorMath",
    version="0.0.2",
    author= "Hansana Prabashwara",
    description="A basic python package for phasor calculation and phasor represention",
    package_dir={"": "app"},
    packages=setuptools.find_packages(where="app"),
    license="MIT",
    long_description = long_description,
    long_description_content_type="text/markdown",
    install_requires=[
      'numpy',
      'plotly',
      'pandas'
    ],
    python_requires='>=3.8',
)