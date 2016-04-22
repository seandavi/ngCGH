from setuptools import setup, find_packages
import sys, os

version = '0.4.4'

readme = open('README.rst','r')

setup(name='ngCGH',
      version=version,
      description="Pseudo-cgh of next-generation sequencing data",
      long_description=readme.read(),
      classifiers=["Topic :: Scientific/Engineering :: Bio-Informatics"], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Sean Davis',
      author_email='sdavis2@mail.nih.gov',
      url='http://github.com/seandavi/ngCGH',
      license='GPL-2',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'pysam>=0.3.0'
      ],
      scripts = ['scripts/ngCGH',
                 'scripts/convert2nexus',
                 'scripts/cgi2nexus',
                 'scripts/cgh2seg'],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
