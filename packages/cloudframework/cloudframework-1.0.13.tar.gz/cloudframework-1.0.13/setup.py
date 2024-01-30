import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cloudframework",
    version="1.0.13",
    author="CloudFramework Team",
    author_email="tools@cloudframework.io",
    description="CloudFramework for Appengine using python language.",
    long_description="This framework has been created to make easier the API creation and backend logic to deploy over GCP Appengine Serverless solution. You are free to use Native python or other libraries when you want. We hope you enjoy it :).",
    long_description_content_type="text/markdown",
    url="https://github.com/CloudFramework-io/appengine-python-core-3.9",
    packages=setuptools.find_packages(),
    install_requires=[
        'Flask==3.0.0', 'psutil'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
