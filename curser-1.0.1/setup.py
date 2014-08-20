#!/usr/bin/python
# -*- coding: utf-8 -*-

from distutils.core import setup

with open("src/curser/README/README.rst",'r') as file :
  long_description = file.read()

setup(name='curser',version='1.0.1',
      url='https://github.com/mrcyberfighter/curser',
      
      author="Eddie Bruggemann",author_email="mrcyberfighter@gmail.com",
      maintainer="Eddie Bruggemann",maintainer_email="mrcyberfighter@gmail.com",
      
      long_description=long_description,
      
      description='''curser is a module based and complementary to pygame:
      an turtle implementation for the pygame module.
      With appeareance,control,drawing,orientation and coordinates retrieving functions.''',
      packages=['curser'],
      package_dir={'curser': 'src/curser'},
      package_data={'curser': ['curser/*.py','Doc/*.txt','Doc/*.zip','License/*.txt']},
      data_files=[('curser',["src/curser/Doc/README.txt","src/curser/License/License.txt","src/curser/README/README.rst"]),('curser/Examples',["src/curser/Examples/curser_example_face.py","src/curser/Examples/curser_example_fractals.py","src/curser/Examples/curser_example_koch.py","src/curser/Examples/curser_example_spirals.py"])],
      platforms=["Linux","Windows"],license="GPL3")



