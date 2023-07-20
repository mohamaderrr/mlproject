from setuptools import find_packages,setup
from typing import List

HYPEN_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    requiremnts=[]

    with open(file_path) as file_obj:
        requiremnts=file_obj.readlines()
        requiremnts= [req.replace("\n","") for req in requiremnts]
        if HYPEN_DOT in requiremnts:
            requiremnts.remove(HYPEN_DOT)
    return requiremnts



setup(


    name='mlproject',
    version='0.0.1',
    author='er-raouan',
    author_email='mohamader14@outlook.fr',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)