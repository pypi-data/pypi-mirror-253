from setuptools import setup, find_packages


requirements = open("requirements.txt").readlines()

setup(
    name="thoughtful-common-packages",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    description="The package contains all frequently used packages in Thoughtful",
    keywords="thoughtful-common-packages",
    url="https://www.thoughtful.ai/",
    version="0.0.5",
)
