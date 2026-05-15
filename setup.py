'''
The setup.py file is an essential part of packaging and
distribution Python projects. It is used by setuptools
(or distutils in older Python versions) to define the configuration
of your project, such as its metadata, dependencies, and more.
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''
    This function reads the requirements.txt file and 
    returns a list of dependencies.
    '''
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # Read lines from the file
            lines=file.readlines()
            # Process each line
            for line in lines:
                requirement=line.strip()
                # ignore empty lines and -e .
                if requirement and requirement!="-e .":
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found. Please ensure it exists in the project directory.")

    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Aniruddha Alkari",
    author_email="aniruddha.alkari@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)