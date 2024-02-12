from setuptools import setup , find_packages
from typing import List

NAME="Housing Model"
VERSION="0.0.2"
DESC="machine learning project-house price prediction"
AUTHOR="Hema Srinivsulu"
EMAIL="hemasrinivasulu.ds@gmail.com"

filename="requirements.txt"

HYPHEN_E_DOT="-e ."

def get_requirements(filepath:str)->List[str]:
    requirements=[]
    with open(filepath) as f:
        requirements=f.readlines()
        requirements=[i.replace("\n","") for i in requirements]
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(name=NAME,
      version=VERSION,
      description=DESC,
      author=AUTHOR,
      author_email=EMAIL,
      packages=find_packages(),
      install_requires=get_requirements(filename)
      )
