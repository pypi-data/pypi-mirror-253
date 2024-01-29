from setuptools import setup
from setuptools import find_packages

exec(open('resellerinterface_api_client_python/_version.py').read())

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='resellerinterface-api-client-python',
    version=__version__,
    description='Python API Client',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='ResellerInterface',
    packages=find_packages(),
    install_requires=[
        'httpx>=0.26.0',
    ],
    license='MIT'
)
