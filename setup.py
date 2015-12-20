from distutils.core import setup
from Cython.Build import cythonize

setup(name="day_20_c", ext_modules=cythonize("day_20_c.pyx"),)
