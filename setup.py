from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    requitements=[]
    with open(file_path) as file_obj:
        requitements = file_obj.readlines()
        requitements = [req.replace("\n","") for req in requitements]

        if(HYPEN_E_DOT in requitements):
            requitements.remove(HYPEN_E_DOT)
    return requitements

setup(
name='MLOps',
version='0.0.1',
author='Rajesh',
author_email='rajeshsk@hotmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)