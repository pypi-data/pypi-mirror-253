from setuptools import setup, find_packages

setup(
    name="thoughtful-common-packages",
    packages=find_packages(),
    install_requires=[
        "rpaframework==28.0.0",
        "python-docx<0.9.0,>=0.8.11",
        "boto3==1.26.129",
        "thoughtful>=2.2,<3.0",
        "pandas==2.1.3",
        "numpy==1.26.1",
        "retry==0.9.2",
        "ta-bitwarden-cli==0.11.0",
        "pillow==10.2.0",
    ],
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
    version="0.0.3",
)
