from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="kedro-expectations",
    version="0.4.1",
    url="https://gitlab.com/anacision/kedro-expectations.git",
    author="anacision GmbH",
    author_email="tech@anacision.de",
    description="Combine Kedro data science pipelines with Great Expectations data validations.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    license="MIT",
    install_requires=[
        "kedro~=0.19",
        "kedro-datasets~=2.0",
        "great_expectations>=0.18.1",
        "pandas"
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    entry_points={
        "kedro.global_commands": ["kedro-expectations = kedro_expectations:commands"]
    }
)
