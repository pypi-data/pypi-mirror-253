import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

required = [
    "mysql-connector-python",
    "python-dotenv",
    "sentry_sdk",
]

setuptools.setup(
    name="xrx_mysql_utils",
    version="1.0.6",
    # author="Fredrik Haglund",
    # author_email="fredrik.haglund@xerox.com",
    description="A mysql utility package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=required,
)
