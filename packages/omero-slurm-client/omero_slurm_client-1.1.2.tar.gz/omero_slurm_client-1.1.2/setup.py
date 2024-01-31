from setuptools import setup
import os


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    description="deprecated omero_slurm_client package, use biomero instead",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    name="omero_slurm_client",
    version="1.1.2",
    install_requires=["biomero"],
    author="T.T. Luik",
    author_email="t.t.luik@amsterdamumc.nl",
    classifiers=["Development Status :: 7 - Inactive"],
    url='https://nl-bioimaging.github.io/biomero/'
)
