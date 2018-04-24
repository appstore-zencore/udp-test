import os
from io import open
from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.rst"), "r", encoding="utf-8") as fobj:
    long_description = fobj.read()

requires = [
    "click",
]

setup(
    name="udp-test",
    version="0.1.0",
    description="A simple udp server and client for network testing.",
    long_description=long_description,
    url="https://github.com/appstore-zencore/udp-test",
    author="zencore",
    author_email="dobetter@zencore.cn",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords=["udp-test"],
    requires=requires,
    install_requires=requires,
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=["udp_test"],
    entry_points={
        "console_scripts": [
            "udp-test = udp_test:test",
            "udp-test.py =  udp_test:test",
            ]
    },
)