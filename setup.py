from setuptools import find_packages,setup
from typing import List
import os

HYPEN_E_DOT='-e .'

# function to get the libraries from requirements.txt
def get_requirements(file_path):
    requirements = []
    with open(file_path) as fp:
        requirements = fp.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements


setup(
    name='student_performance',
    version='1.0.0',
    author='surya',
    author_email='suryakadali1994@gmail.com',
    install_requires=get_requirements(os.path.join('requirements.txt')),
    packages=find_packages()

)