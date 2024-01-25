from setuptools import setup
import os

VERSION = "0.0.1"

def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="spql",
    description="Lorem Ipsum",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Florents Tselai",
    url="https://github.com/Florents-Tselai/spql",
    entry_points="""
        [console_scripts]
        spql=spql.cli:cli
    """,
    project_urls={
        "Issues": "https://github.com/Florents-Tselai/spql/issues",
        "CI": "https://github.com/Florents-Tselai/spql/actions",
        "Changelog": "https://github.com/Florents-Tselai/spql/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["spql"],
    install_requires=[ "click", "setuptools", "pip"],
    extras_require={"test": ["pytest", "pytest-cov", "black", "ruff", "click"]},
    python_requires=">=3.7"
)
