from setuptools import setup, find_packages

setup(
    name='pushover_package',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    
    description='A simple Python wrapper for the Pushover API',
    keywords='pushover notification api',
)
