from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='verycomplexapp',
      version=version,
      description="Maybe not so complex",
      long_description="""\
I was just showing off""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='python setuptools',
      author='Alberto Aguilera',
      author_email='drimer.aaj',
      url='www.albertoaj.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points={
          'console_scripts': (
              'command_1 = verycomplexapp.main:complex_command_1',
          )
      },
      )
