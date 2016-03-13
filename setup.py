#!/usr/bin/env python

"""
Setting up program for Apyori.
"""

import apyori
import setuptools


setuptools.setup(
    name='apyori',
    description='Simple Apriori algorithm Implementation.',
    version=apyori.__version__,
    author=apyori.__author__,
    author_email=apyori.__author_email__,
    py_modules=['apyori'],
    test_suite='nose.collector',
    tests_require=['nose', 'mock'],
    entry_points={
        'console_scripts': [
            'apyori-run = apyori:main',
        ],
    },
    classifires=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
