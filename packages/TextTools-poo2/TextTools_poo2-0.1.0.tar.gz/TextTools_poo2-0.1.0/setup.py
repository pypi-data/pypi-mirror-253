from setuptools import setup, find_packages

setup(
name='TextTools_poo2',
version='0.1.0',
author='Marcos, Anna',
author_email='annabeatriz_2019@outlook.com',
packages=find_packages(),
include_package_data=True,
install_requires=[
    'Click',
],
entry_points='''
        [console_scripts]
        texttools=TextTools.main:cli
    ''',
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent',
],
python_requires='>=3.6',
)