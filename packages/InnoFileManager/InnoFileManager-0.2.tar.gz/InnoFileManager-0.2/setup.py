from setuptools import setup, find_packages

setup(\
    name='InnoFileManager',

    version='0.2',

    url='https://github.com/AmZakirov/FileManager',

    license='',

    author='AmZakirov',

    author_email='am.zakirov@innopolis.university',

    description='Easy way to manage files',

    packages=find_packages(exclude=['tests']),

    long_description=open('README.md').read(),

    zip_safe=False)
