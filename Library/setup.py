from setuptools import setup

setup(name = 'pear',
      version = '0.1',
      description = 'The library that makes neural networks appear',
      url = '',
      author = 'Candice Bentejac, Anna Csorgo, Daniel Hajto',
      author_email = '',
      license = 'BSD-3-Clause',
      packages = ['pear'],
      install_requires = ['numpy', 'matplotlib', 'pillow', 'tensorflow'],
      zip_safe = False)

