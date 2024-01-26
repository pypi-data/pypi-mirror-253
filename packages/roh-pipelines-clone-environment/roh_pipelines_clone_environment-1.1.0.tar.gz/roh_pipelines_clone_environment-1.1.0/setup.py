from setuptools import setup, find_packages

setup(
    name='roh_pipelines_clone_environment',
    version='1.1.0',
    description='Clone a deployment environment in a Bitbucket repository with pipelines enabled',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=['requests'],
    entry_points={
      'console_scripts': [
        'clone-environment = roh_pipelines.clone_environment:main',
      ],
    },
)