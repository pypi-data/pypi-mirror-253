import pathlib

from setuptools import find_namespace_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="unstract-sdk",
    # The version of the unstract-sdk package is used at runtime to
    # validate manifests.
    # That validation must be updated if our semver format changes
    # such as using release candidate versions.
    version="0.3.5",
    description="A framework for writing Unstract Tools/Apps",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://unstract.com/sdk",
    author="Zipstack Inc",
    author_email="devsupport@zipstack.com",
    license="MIT",
    packages=find_namespace_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "filetype==1.2.0",
        "jsonschema~=4.18.2",
        "llama-index==0.9.28",
        "pdfplumber==0.10.3",
        "pypandoc==1.12",
        "pytesseract==0.3.10",
        "python-dotenv==1.0.0",
        "qdrant-client==1.7.0",
        "tiktoken~=0.4.0",
        "transformers==4.37.0",
        "unstract-connectors~=0.0.2",
        "unstract-adapters~=0.0.2",
        "parameterized==0.9.0",
    ],
    extras_require={"docs": ["lazydocs~=0.4.8"]},
    classifiers=[
        # This information is used when browsing on PyPi.
        # Dev Status
        "Development Status :: 3 - Alpha",
        # Project Audience
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        # Python Version Support
        "Programming Language :: Python :: 3.9",
    ],
    keywords="unstract tools-development-kit apps -development-kit sdk",
    python_requires="<=3.11",
    scripts=["bin/unstract-tool-gen"],
)
