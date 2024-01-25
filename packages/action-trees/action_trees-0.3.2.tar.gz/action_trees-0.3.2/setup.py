# type: ignore

"""The setup script."""


import codecs
import os
import os.path

from setuptools import find_packages, setup


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


requirements = []

test_requirements = [
    "pytest>=3",
]

setup(
    author="Jev Kuznetsov",
    author_email="jev@roxautomation.com",
    setup_requires=["setuptools_scm"],
    python_requires=">=3.11",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.11",
    ],
    description="Action decomposition and execution framework",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    install_requires=requirements,
    include_package_data=True,
    keywords="",
    name="action_trees",
    package_dir={"": "src"},
    packages=find_packages("src"),
    test_suite="tests",
    tests_require=test_requirements,
    url="",
    # Use setuptools_scm for versioning
    use_scm_version={
        "write_to": "src/action_trees/version.py",
        "fallback_version": "0.0.0+unknown",
    },
    # zip_safe=False,
    entry_points={"console_scripts": ["action_trees=action_trees.cli:cli"]},
)
