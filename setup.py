from setuptools import setup, find_packages
from typing import List
def get_requirements()->List[str]:
    """
    This function returns a list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        #open the requirements.txt file
        with open('requirements.txt','r') as file:
            #read lines from file
            lines=file.readlines()
            #process each line
            for line in lines:
                requirement=line.strip()
                #ignore empty lines and -e
                if requirement and requirement!="-e .":
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    return requirement_lst
# print(get_requirements())
setup(
    name="NetworkSecurity",
    version='0.0.1',
    author="Ujjwal Raj",
    author_email="ujjwalrajbgis@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
    description="A Network Security project",
)
