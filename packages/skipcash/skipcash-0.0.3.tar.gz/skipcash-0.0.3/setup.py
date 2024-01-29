from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="skipcash",
    version="0.0.3",
    packages=find_packages(),
    long_description_content_type='text/markdown',
    long_description=long_description,
    description="The SkipCash SDK for Python enables developers to easily integrate SkipCash payment services into their Python applications.",
    install_requires=[
        "annotated-types",
        "certifi",
        "charset-normalizer",
        "idna",
        "pip",
        "pycountry",
        "requests",
        "setuptools",
        "urllib3",
        "wheel"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
    ],
    author="Muhammad Arshad",
    author_email="arshad@codelounge.io",
    keywords='SkipCash Python SDK, skipcash, skipcash-sdk, skipcash-python',
    url='https://codelounge.io',
    company_name="CODELOUNGE (SMC) PRIVATE LIMITED"
)