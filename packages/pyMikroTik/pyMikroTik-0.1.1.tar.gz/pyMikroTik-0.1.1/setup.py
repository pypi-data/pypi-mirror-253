from setuptools import setup, find_packages


"""
:authors: Fialkofskiy
:copyright: (c) 2024 Fialkofskiy
"""

version = '0.1.1'
long_description = '''pyMikroTik is a powerful tool for interacting with MikroTik routers, 
providing convenient and flexible device management through SSH connections. 
Developed in Python, the library offers a straightforward interface for performing various operations, 
including parameter configuration, monitoring, and task automation.'''
description = 'pyMikroTik is a powerful tool for interacting with MikroTik routers'


with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='pyMikroTik',
    version=version,

    author='fialkofskiy',
    author_email='fialkofskiy@gmail.com',

    long_description=long_description,
    description=description,

    packages=find_packages(),
    install_requires=[
        'bcrypt==4.1.2',
        'cffi==1.16.0',
        'cryptography==42.0.1',
        'paramiko==3.4.0',
        'pycparser==2.21',
        'PyNaCl==1.5.0'
    ]
)


