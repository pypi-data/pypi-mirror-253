from setuptools import setup, find_packages

with open('README.md', encoding='utf8') as f:
    readme = f.read()

requirements = ["httpx>=0.26.0"]
setup(
    name="rootpay_sdk",
    version="0.0.6",
    author="Touka",
    author_email="touka.touka@icloud.com",
    description="A package to interact with root-pay.app API",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/muzonff/root-pay_sdk",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
