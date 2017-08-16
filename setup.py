# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

setup(
      name="TrandSimplied",
      version="0.10",
      description="traditional to simplied, simplied to traditional",
      author="ShawnXUNJU,  CZF",
      license="LGPL",
      packages= find_packages(),
      package_data={'':['data/*.txt']},
      # data_files=[('data_ffffff', ['TrandSimplied/data/ft.txt'])]
      )