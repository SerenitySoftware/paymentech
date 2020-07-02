"""Python SDK for Chase Paymentech"""
import setuptools


with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

with open("VERSION", "r") as version_file:
    version = version_file.read().strip()

setuptools.setup(
    name="paymentech",
    version=version,
    author="Jordan Ambra",
    author_email="jordan@serenity.software",
    description="Python SDK for Chase Paymentech",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SerenitySoftware/paymentech",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "License :: Freely Distributable"
    ],
    keywords=['chase', 'paymentech', 'e-commerce', 'payments'],
    install_requires=['requests'],
    package_data={'paymentech': ['templates/*.xml']}
)
