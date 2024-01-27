from setuptools import setup, find_packages

setup(
    name='pushover_package',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    py_modules=['pushover'],
    
    description='A simple Python wrapper for the Pushover API',
    keywords='pushover notification api',
)
