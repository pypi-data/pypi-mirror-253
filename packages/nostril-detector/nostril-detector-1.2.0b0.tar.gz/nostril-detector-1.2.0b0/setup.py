#!/usr/bin/env python3
# =============================================================================
# @file    setup.py
# @brief   Nostril setup file
# @author  Michael Hucka <mhucka@caltech.edu>
# @license Please see the file named LICENSE in the project directory
# @website https://github.com/casics/nostril
# =============================================================================

import os
from   os import path
from   setuptools import setup
import sys

here = path.abspath(path.dirname(__file__))

# with open(path.join(here, 'requirements.txt')) as f:
#     reqs = f.read().rstrip().splitlines()

reqs = [
    'plac>=0.9.1',
    'tabulate>=0.7.7',
    'humanize>=0.5.1',
    'pytest>=3.0.5',
]

# The following reads the variables without doing an "import nostril_detector-detector",
# because the latter will cause the python execution environment to fail if
# any dependencies are not already installed -- negating most of the reason
# we're using setup() in the first place.  This code avoids eval, for security.

version = {}
with open(path.join(here, 'nostril_detector/__version__.py')) as f:
    text = f.read().rstrip().splitlines()
    vars = [line for line in text if line.startswith('__') and '=' in line]
    for v in vars:
        setting = v.split('=')
        version[setting[0].strip()] = setting[1].strip().replace("'", '')

# Finally, define our namesake.

setup(
    name             = version['__title__'].lower(),
    description      = version['__description__'],
    long_description = 'Nostril (Nonsense String Evaluator) implements a heuristic mechanism to infer whether a given word or text string is likely to be meaningful or nonsense.',
    version          = version['__version__'],
    url              = version['__url__'],
    author           = version['__author__'],
    author_email     = version['__email__'],
    license          = version['__license__'],
    keywords         = "program-analysis text-processing gibberish-detection identifiers",
    packages         = ['nostril_detector'],
    scripts          = ['bin/nostril_detector'],
    package_data     = {'nostril_detector': ['ngram_data.pklz']},
    install_requires = reqs,
    platforms        = 'any',
    python_requires  = '>=3',
)
