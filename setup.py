from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='ngCGH',
      version=version,
      description="Pseudo-cgh of-generation sequencing data",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Sean DAvis',
      author_email='sdavis2@mail.nih.gov',
      url='',
      license='GPL-2',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
