#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Setup file for wiki.

    This file was generated with PyScaffold 2.5.6, a tool that easily
    puts up a scaffold for your new Python project. Learn more under:
    http://pyscaffold.readthedocs.org/
"""

import sys
from setuptools import setup
import versioneer


def setup_package():
    needs_sphinx = {'build_sphinx', 'upload_docs'}.intersection(sys.argv)
    sphinx = ['sphinx'] if needs_sphinx else []
    setup(setup_requires=['six', 'pyscaffold>=2.5a0,<2.6a0'] + sphinx,
          version=versioneer.get_version(),
          cmdclass=versioneer.get_cmdclass(),
          use_pyscaffold=True)


if __name__ == "__main__":
    setup_package()
