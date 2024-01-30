import os

from setuptools import setup, find_packages


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='fdnubank',
    version='0.0.2',
    url='https://github.com/andreroggeri/pynubank',
    author='fdoooch',
    author_email='fdoooch@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'fdnubank': ['queries/*.gql', 'utils/mocked_responses/*.json']},
    install_requires=required,
    setup_requires=['pytest-runner'],
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    entry_points={
        'console_scripts': [
            'pynubank = pynubank.cli:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.11',
    ]
)