"""Python SDK for Chase Paymentech"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="paymentech",
    version="0.0.2",
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
