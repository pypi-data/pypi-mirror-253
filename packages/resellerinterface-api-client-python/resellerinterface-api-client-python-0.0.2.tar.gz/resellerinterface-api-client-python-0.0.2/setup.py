from setuptools import setup
from setuptools import find_packages

exec(open('resellerinterface_api_client_python/_version.py').read())

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='resellerinterface-api-client-python',
    version=__version__,
    description='Python API Client',
    url='https://github.com/resellerinterface/api-client-python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='ResellerInterface',
    packages=find_packages(),
    install_requires=[
        'httpx>=0.26.0',
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP'
    ],
    license='MIT'
)
