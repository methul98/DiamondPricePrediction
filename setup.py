from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        # we will get \n with all line
        requirements=[req.replace('\n','') for req in requirements]
        # -e . willl use to build setup.py while run requirements
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='RegressionProject',
    version='0.0.1',
    author='Methul',
    author_email='methul6119097@gmail.com',
    install_requires=['numpy','pandas'],
    packages=find_packages()
)