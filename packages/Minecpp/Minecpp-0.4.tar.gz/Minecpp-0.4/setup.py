from setuptools import setup, find_packages
import os
from pathlib import Path


# parent_dir = Path(__file__).resolve().parent

def find_all_dirs_and_paths(parent_dir):
    all_dirs = []
    
    for dirpath, dirnames, filenames in os.walk(parent_dir):
        for dirname in dirnames:
            dir_full_path = os.path.join(dirpath, dirname, '*')
            all_dirs.append(dir_full_path.strip('Minecpp/'))

    return all_dirs

# Replace 'parent_directory' with the path to your parent directory
parent_directory = 'Minecpp'

directories = find_all_dirs_and_paths(parent_directory)

# print(directories)

# print(directories)

setup(
    name='Minecpp',
    version='0.4',
    description='MineCPP - A tool to mine a GitHub repository and obtain a dataset containing a list of bug-fix pairs and related information.',
    long_description=open('Readme.md').read(),
    long_description_content_type='text/markdown',
    packages=['Minecpp'],
    include_package_data=True,
    package_data={
        'Minecpp': directories,# Include all files in the 'Minecpp' directory
    },
    install_requires=[
        'chardet==4.0.0',
        'code_bert_score==0.4.1',
        'crystalbleu==0.1',
        'lizard==1.17.10',
        'nltk==3.8.1',
        'pandas==2.0.3',
        'PyDriller==2.6',
        'torch==2.1.2',
        'transformers==4.36.0',
        'tree_sitter==0.20.4',
        'tqdm',
        'flask',
        'matplotlib',
        # list your dependencies here
    ],
    entry_points={
        'console_scripts': [
            'minecpp = Minecpp.main:main',  # adjust module and function names
        ],
    },
)
