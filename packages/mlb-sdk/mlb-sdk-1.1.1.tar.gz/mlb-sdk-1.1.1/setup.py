from setuptools import setup, find_packages

# with open("./requirements.txt") as f:
#     requirements = f.read().split("\n")

with open('./README.md', 'r') as f:
    long_description = f.read()
    
setup(
    name="mlb-sdk",
    version='1.1.1',
    description='Python wrapper for MLB APIs',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ryan Schreiber',
    author_email='ryanschreiber86@gmail.com',
    packages=find_packages(),
    install_requires=["requests"],
    keywords="mlb major league baseball sdk mlb-sdk sports professional",
    project_urls={
    'Documentation': 'https://github.com/mlb-sdk/python-mlb-sdk/',
    'Source': 'https://github.com/mlb-sdk/python-mlb-sdk/',
    'Tracker': 'https://github.com/mlb-sdk/python-mlb-sdk/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.0')
