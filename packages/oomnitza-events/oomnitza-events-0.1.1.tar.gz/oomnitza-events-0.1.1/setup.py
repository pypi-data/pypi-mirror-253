import setuptools

from pathlib import Path

from oomnitza_events import version

requirements = [
    "analytics-python==1.2.9",
    "arrow",
    "Cerberus",
    "psycopg2-binary==2.8.6",
    "typing_extensions",
]

dev_requirements = [
    "pytest",
    "pytest-pep8",
    "pytest-cov",
    "wheel",
]

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="oomnitza-events",
    version=version.__version__,
    packages=setuptools.find_packages(exclude=["tests"]),
    description="This project is developed for tracking Oomnitza activities.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Oomnitza",
    author_email="etl-admin@oomnitza.com",
    install_requires=requirements,
    extras_require={
        "dev": dev_requirements,
    },
)
