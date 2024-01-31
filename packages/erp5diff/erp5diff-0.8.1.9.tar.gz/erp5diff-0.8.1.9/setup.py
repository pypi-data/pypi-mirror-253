#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from setuptools import setup, find_packages
import re


def read(name):
  with open(name) as f:
    return f.read()

api_version = re.search(r'\s*__version__\s*=\s*(\S+)',
                        read('src/ERP5Diff/ERP5Diff.py')).group(1).strip()
revision = 9
version = '%s.%s' % (api_version.replace("'", ''), revision)


long_description=(
        read('README.rst')
        + '\n' +
        read('CHANGES.rst')
    )

setup(name="erp5diff",
      version=version,
      description="XUpdate Generator for ERP5",
      long_description=long_description,
      author="Yoshinori OKUJI",
      author_email="yo@nexedi.com",
      url="https://lab.nexedi.com/nexedi/erp5diff/",
      license="GPL",
      packages=find_packages('src'),
      package_dir={'': 'src'},
      entry_points={'console_scripts': ["erp5diff = ERP5Diff:main"]},
      data_files=[('share/man/man1', ['src/erp5diff.1'])],
      install_requires=['lxml', 'six', 'zope.interface'],
      classifiers=['License :: OSI Approved :: GNU General Public License (GPL)',
                  'Operating System :: OS Independent',
                  'Topic :: Text Processing :: Markup :: XML',
                  'Topic :: Utilities'],
      include_package_data=True,
      zip_safe=False,
     )
