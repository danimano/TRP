from setuptools import setup

setup(name = 'pear',
      version = '0.1',
      description = 'The library that makes neural networks appear',
      url = 'https://github.com/danimano/TRP',
      author = 'Candice Bentejac, Anna Csorgo, Daniel Hajto',
      author_email = 'candice.bentejac@etu.u-bordeaux.fr',
      license = 'BSD-3-Clause',
      packages = ['pear'],
      install_requires = ['numpy', 'matplotlib', 'pillow', 'tensorflow'],
      zip_safe = False)

