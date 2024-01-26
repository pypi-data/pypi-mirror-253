import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="voidray-pkg-scdev-pd-columns",
    version="0.0.1",
    author="Schooldevops",
    author_email="schooldevops@gmail.com",
    description="schooldevops sample lib",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/schooldevops/python-tutorials",
    project_urls={
        "Bug Tracker": "https://github.com/schooldevops/python-tutorials/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)

# [pypi]
#   username = __token__
#   password = pypi-AgEIcHlwaS5vcmcCJGNjYTM5MjgxLTY4NDctNDZiNC05ZTI2LWMyODgwNDY2NmUzOQACKlszLCI4ODhmMDRkMC00MTYxLTQ3ZmYtYWJjMC1iMTVhN2Q3YzczYzQiXQAABiCEgDAEM7q4aQiSuCNrUGi76kg0eFs21mhbSqqxFXXjzw