import os

import setuptools


class CleanCommand(setuptools.Command):
    """Custom clean command to tidy up the project root."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open('requirements.txt') as fin:
    requirements = fin.read()

setuptools.setup(
    name="generalindex",
    version="0.2.1",
    author="General Index",
    author_email="info@general-index.com",
    description="Python SDK for the General Index platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.general-index.com/",
    packages=setuptools.find_packages(exclude=["test"]),
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent"
                 ],
    install_requires=[
        requirements
    ],
    python_requires='>=3.9',
    cmdclass={
        'clean': CleanCommand,
    }
)
