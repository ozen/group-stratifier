from setuptools import setup, find_packages

setup(
    name='group_stratifier',
    version='0.2.0',
    description='Stratified K-Folds cross-validator with non-overlapping groups using genetic algorithm',
    author='Yigit Ozen',
    license="MIT",
    url='https://github.com/ozen/group-stratifier',
    packages=find_packages(),
    install_requires=['numpy>=1.17.0', 'pyeasyga'],
)
