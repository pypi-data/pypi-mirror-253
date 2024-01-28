from glob import glob
from os.path import basename, sep
from os.path import splitext

from setuptools import setup
from setuptools import find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()


with open("README.md", "r", encoding="utf-8") as fp:
    readme = fp.read()

setup(
    name="jener",
    version="1.0.5",
    description="Japanese Extended Named Entity Recognizer",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="k141303",
    author_email="kouta.nakayama@gmail.com",
    maintaner="k141303",
    maintaner_email="kouta.nakayama@gmail.com",
    packages=["jener", "jener.model", "jener.utils", "jener.model.loss", "jener.model.utils"],
    package_dir={"": "src"},
    url="https://github.com/k141303/JENER",
    download_url="https://github.com/k141303/JENER",
    include_package_data=True,
    install_requires=["torch>=1.13.0",
        "hydra-core>=1.2.0",
        "tqdm>=4.64.1",
        "liat_ml_roberta",
        "torch_struct",
        "transformers>=4.22.1",
    ],
)
