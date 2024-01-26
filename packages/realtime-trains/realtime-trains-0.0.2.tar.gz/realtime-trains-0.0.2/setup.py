from setuptools import find_packages, setup

with open("README.md", "r") as f:
	long_description = f.read()

setup(
    name="realtime-trains",
    version="0.0.2",
    description="Unofficial Python API for Realtime Trains",
    package_dir={"": "realtime_trains"},
	packages=find_packages(where="realtime_trains"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mbukovac/realtime-trains",
    author="Marko B.",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    include_package_data=True,
    install_requires=["httpx", "pydantic"]
)
