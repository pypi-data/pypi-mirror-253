from setuptools import setup, find_packages

setup(
    name='skymap_job_processing',
    version='0.6.0',
    packages=find_packages(),
    install_requires=[
        "requests",
        "websockets"
    ],
)