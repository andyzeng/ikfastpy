from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(ext_modules=[Extension("ikfastpy", 
                            ["ikfastpy.pyx", 
                             "ikfast_wrapper.cpp"], language="c++", libraries=['lapack'])],
      cmdclass = {'build_ext': build_ext})