from setuptools import setup

with open('readme.MD') as f:
    long_description = f.read()

setup(
    name='twikit',
    version='0.0.2',
    install_requires=['httpx'],
    description='Twitter api wrapper for python.',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
