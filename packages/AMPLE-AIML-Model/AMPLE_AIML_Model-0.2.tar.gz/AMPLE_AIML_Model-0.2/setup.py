from setuptools import setup, find_packages
from pkg_resources import parse_requirements

# Parse the requirements from requirements.txt
with open('requirements.txt') as f:
    requirements = [str(req) for req in parse_requirements(f)]

setup(
    name='AMPLE_AIML_Model',
    version='0.2',
    packages=find_packages(),
    install_requires=requirements,
)
