import setuptools

setuptools.setup(
    name = "hensho",
    version = "0.0.1a",
    author = "Ben",
    description = "short package description",
    classifiers = [
        "Programming Language :: Python :: 3",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6"
)