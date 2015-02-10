# -*- coding: utf-8 -*-
import versioneer
from setuptools import setup, find_packages

versioneer.VCS = 'git'
versioneer.versionfile_source = 'homeslice/_version.py'
versioneer.versionfile_build = 'homeslice/_version.py'
versioneer.tag_prefix = ''
versioneer.parentdir_prefix = 'homeslice-'

with open('README.rst') as f:
    readme = f.read()

setup(
    name='homeslice',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Manage your $HOME with Git and a little Python.',
    long_description=readme,
    author='Dave Forgac',
    author_email='tylerdave@tylerdave.com',
    url='https://github.com/tylerdave/homeslice',
    packages=find_packages(),
    include_package_data=False,
    install_requires=[],
    license='MIT',
    classifiers=(
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3'
        )

)
