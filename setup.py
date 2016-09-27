from setuptools import setup, find_packages

package = 'spec-py'
version = '0.1'

INSTALL_REQUIRES = ['toolz>=0.8']

setup(name=package,
      version=version,
      packages=find_packages(),
      description="Simple specification",
      url='')
