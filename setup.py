import glob
import os
import sys

from setuptools import setup
from distutils.sysconfig import get_python_lib


if os.path.exists('readme.rst'):
    print("""The setup.py script should be executed from the build directory.

Please see the file 'readme.rst' for further instructions.""")
    sys.exit(1)


setup(
    name = "libasynctasks",
    package_dir = {
        '': 'src'
    },
    data_files = [
        (get_python_lib(), glob.glob('src/*.so')),
    ],
    author = 'Caleb Marshall',
    description = 'A fast, efficient task based system for concurrency.',
    license = 'Apache',
    keywords = 'cmake cython build',
    url = 'https://github.com/AnythingTechPro/libasynctasks',
    zip_safe = False
)
