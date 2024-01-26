import numpy as np
from Cython.Build import cythonize
from setuptools import Extension, setup

setup(
    ext_modules=cythonize(
        [
            Extension(
                "bbob_functions",
                ["bbob_functions.pyx"],
                include_dirs=[np.get_include()],
            )
        ]
    )
)
