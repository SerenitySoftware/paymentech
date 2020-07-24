"""Python SDK for Chase Paymentech"""
import os
import setuptools


with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

version_path = os.path.join(os.path.split(__file__)[0], "paymentech/version.py")
with open(version_path) as version_file:
    version = ""
    # Execute the code in version.py.
    exec(compile(version_file.read(), version_path, 'exec'))

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
    install_requires=['requests', 'pydantic'],
    package_data={'paymentech': ['templates/*.xml']}
)
