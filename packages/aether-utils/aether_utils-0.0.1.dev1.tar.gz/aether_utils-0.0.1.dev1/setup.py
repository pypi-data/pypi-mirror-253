import setuptools

import aether_utils

# Use requirements.txt to set the install_requires
with open("requirements.txt") as f:
    install_requires = [line.strip() for line in f]


setuptools.setup(
    name=aether_utils.__name__,
    version=aether_utils.__version__,
    author="Richard Edgar, Nicholas King, Harsha Nori",
    author_email="riedgar@microsoft.com",
    description="A Python package for use in Aether Incubation projects.",
    long_description="""Contains various useful utilities for our projects.""",
    long_description_content_type="text/markdown",
    url="https://github.com/microsoft/aether-utils/",
    packages=setuptools.find_packages(),
    python_requires=">=3.10",
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
    ],
    include_package_data=True,
    zip_safe=False,
)
