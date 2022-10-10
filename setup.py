"""The setup file"""
from setuptools import setup, find_packages

setup(
    name='cronparser',
    version='0.1',
    description='The simple cron parser',
    url='http://github.com/yashpokar/cronparser',
    author='Yash Patel',
    author_email='yashpokar143@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'tox' # TODO : make it test dependecy
    ],
    entry_points={
        'console_scripts': ['parsecron=cronparser.cmd:main']
    },
    zip_safe=False
)
