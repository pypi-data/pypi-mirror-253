from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "Python Prime Number Finder"
LONG_DESCRIPTION = "Prime Finder can be used to check a number, find permutations, find factors of a number and much, much more"

setup(
    name = "PrimeFinder",
    version = VERSION,
    author = "Rishit Logar",
    author_email = "logarrishit@gmail.com",
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    packages = find_packages(),
    requires = [],
    keywords = ["Prime Numbers", "Prime Finder", "Prime", "Factors", "Permutation", "Finder", "Primes", "Factors", "Check Factor", "Prime Number", "Combination"],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
        "Operating System :: POSIX :: Linux"
    ])