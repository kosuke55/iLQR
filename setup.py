from setuptools import setup, find_packages

setup(
    name="ilqr",
    version="0.1.0",
    description="A package for iLQR controller",
    author="Bharath chandra",
    author_email="iambharathchandra@gmail.com",
    url="https://github.com/Bharath2/iLQR",
    packages=find_packages(),
    install_requires=["numpy", "numba", "sympy", "matplotlib"],
)
