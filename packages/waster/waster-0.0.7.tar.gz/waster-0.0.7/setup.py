"""Python setup.py for project_name package"""
from pathlib import Path

from setuptools import find_packages, setup


def read(*paths, **kwargs) -> str:
    return Path(*paths).read_text(encoding=kwargs.get('encoding', 'utf8')).strip()


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).splitlines(keepends=False)
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="waster",
    author="Leikt Sol'Reihin",
    # url="https://github.com/Leikt/waster",
    python_requires=">3.10.0",
    description="A simple microservice to test the behaviour of infrastructures.",
    long_description=read("README.rst"),
    long_description_content_type="text/markdown",
    packages=find_packages(include=["waster"]),
    install_requires=read_requirements('./requirements/main.txt'),
    extras_require={
        "test": read_requirements('./requirements/test.txt'),
        "dev": read_requirements('./requirements/dev.txt'),
        "doc": read_requirements('./requirements/doc.txt')
    },
    entry_points={
        "console_scripts": ["waster = waster:main"]
    },

    use_scm_version=True,
    setup_requires=['setuptools_scm']
)
