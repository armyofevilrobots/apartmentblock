"""
 _______                    __                         __
|   _   |.-----.---.-.----.|  |_.--------.-----.-----.|  |_
|       ||  _  |  _  |   _||   _|        |  -__|     ||   _|
|___|___||   __|___._|__|  |____|__|__|__|_____|__|__||____|
         |__|
 ______ __              __
|   __ \  |.-----.----.|  |--.
|   __ <  ||  _  |  __||    <
|______/__||_____|____||__|__|

Pluggable DHCP/Bootp server

"""
from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='apartmentblock',
      version=version,
      description="Pluggable DHCP server",
      long_description="""\
Python based pluggable DHCP server""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='dhcp python pluggable mac ip arp',
      author='Derek Anderson',
      author_email='derek@armyofevilrobots.com',
      url='http://armyofevilrobots.com/',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'dpkt',
          'python-daemon',
          'ConfigObj',
          'netifaces',
          # -*- Extra requirements: -*-
      ],
      entry_points={
          'console_scripts': [
              'apartmentblock = apartmentblock.scripts.dhcp:main',
              ]
          },
      dependency_links=[
          'http://dpkt.googlecode.com/files/dpkt-1.7.tar.gz'
          ]
      )
