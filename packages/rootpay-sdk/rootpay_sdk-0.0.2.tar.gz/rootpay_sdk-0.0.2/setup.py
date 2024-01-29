from setuptools import setup, find_packages

requirements = ["httpx>=0.26.0"]
print(find_packages())
setup(
    name="rootpay_sdk",
    version="0.0.2",
    author="Touka",
    author_email="touka.touka@icloud.com",
    description="A package to interact with root-pay.app API",
    long_description="A package to interact with root-pay (update later)",
    url="https://github.com/muzonff/root-pay_sdk",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
