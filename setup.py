# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

version = '0.1'

tests_require = [
    'pytest',
]

install_requires = [
    'setuptools',
    'portalocker >= 1.1.0',
]

yaml_requires = [
    'PyYAML >= 3.12',
]

rapidjson_requires = [
    'python-rapidjson >= 0.2.7',
]

msgpack_requires = [
    'msgpack-python >= 0.4.8',
]

bson_requires = [
    'bson >= 0.5.0',
]


setup(name='cromlech.marshallers',
      version=version,
      description="A collection of data marshallers for various generic uses",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='Cromlech',
      author='The Cromlecch Team',
      author_email='dolmen@list.dolmen-project.org',
      url='https://github.com/Cromlech',
      license='ZPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['cromlech'],
      include_package_data=True,
      extras_require={
          'test': tests_require,
          'yaml': yaml_requires,
          'rapidjson': rapidjson_requires,
          'msgpack': msgpack_requires,
          'bson': bson_requires,
      },
      zip_safe=False,
      install_requires=install_requires,
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
