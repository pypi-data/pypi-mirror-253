from setuptools import setup

setup(name='PourPy',
      version='0.1',
      description='A Python package for generating potential/pH diagrams',
      url='https://gitlab.com/cmbm-ethz/pourbaix-diagrams',
      author='Fabio Furcas, Anja Korber, Mohit Pundir',
      author_email='mpundir@ethz.ch',
      license='GNU LGPL v3',
      packages=['PourPy'],
      install_requires=[
          'argparse',
          'pytest',
          'bokeh',
          'matplotlib',
          'shapely',
          'nbsphinx',
          'sphinx-autoapi',
          'sphinx_rtd_theme'
      ],
      zip_safe=False)
