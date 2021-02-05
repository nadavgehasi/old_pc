from setuptools import setup, find_packages

setup(
    name="toolip",
    version="0.0.1",
    author="Nadav Gehasi",
    author_email="nadavgehasi@gmail.com",
    description="A small example package",
    url="https://github.com/pypa/sampleproject",
    packages=find_packages(),
    include_package_data=True,
    install_requires=open("requirements.in").readlines(),
    tests_require=open("requirements.testing.in").readlines(),
    python_requires=">=3.8",
)
