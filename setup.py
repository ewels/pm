from setuptools import setup, find_packages
import sys, os

version = '1.0'

try:
    with open("requirements.txt", "r") as f:
        install_requires = [x.strip() for x in f.readlines()]
except IOError:
    install_requires = []

setup(name='pm',
      version=version,
      description="Project and Data management for NGI Sweden",
      long_description='This package contains a set of functionalities that are '
                       'useful in the day-to-day tasks of bioinformatitians in '
                       'National Genomics Infrastructure in Stockholm, Sweden.',
      keywords='bioinformatics',
      author='Guillermo Carrasco',
      author_email='guillermo.carrasco@scilifelab.se',
      url='https://portal.scilifelab.se/genomics/',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      scripts=['scripts/pm'],
      install_requires=install_requires
      )
