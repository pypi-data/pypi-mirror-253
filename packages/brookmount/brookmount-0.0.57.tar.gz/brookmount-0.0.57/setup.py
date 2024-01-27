from setuptools import setup, find_packages

setup(
    name='brookmount',
    version='0.0.57',
    packages=find_packages(),
    install_requires=[
        
    ],
    entry_points={
        'console_scripts': [
            'brookmount = brookmount.sac:sac',
        ],
    },
    author='reyan',
    description='python package for brookmount.',
    url='https://github.com/brookmount/pip',
)
