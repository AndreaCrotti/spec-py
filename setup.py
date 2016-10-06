from setuptools import setup, find_packages

package = 'spec'
version = '0.1'

INSTALL_REQUIRES = ['toolz>=0.8', 'voluptuous>=0.8.7']

setup(name=package,
      version=version,
      packages=['spec'],
      description="Simple specification",
      license='MIT',
      author="Andrea Crotti",
      author_email="andrea.crotti.0@gmail.com",
      install_requires=INSTALL_REQUIRES,
      classifiers=[
          "Development Status :: 3 - ALpha",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: Implementation :: CPython",
          "Programming Language :: Python :: Implementation :: PyPy"],
      url='https://github.com/AndreaCrotti/spec')
