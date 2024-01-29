#!/usr/bin/env python3
from setuptools import setup

from src.midpoint_cli import __version__

setup(
    name='midpoint-cli',
    version=__version__,
    packages=['midpoint_cli', 'midpoint_cli.client', 'midpoint_cli.prompt'],
    package_dir={'midpoint_cli': 'src/midpoint_cli',
                 'midpoint_cli.client': 'src/midpoint_cli/client',
                 'midpoint_cli.prompt': 'src/midpoint_cli/prompt'
                 },
    scripts=['src/midpoint-cli'],
    test_suite='test',
    setup_requires=['pytest-runner'],
    install_requires=['clint==0.5.1', 'requests==2.25.1', 'tabulate==0.8.9'],
    tests_require=['pytest'],
    url='https://gitlab.com/alcibiade/midpoint-cli',
    license='MIT',
    author='Yannick Kirschhoffer',
    author_email='alcibiade@alcibiade.org',
    description='A command line client to Midpoint Identity Management system.',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: System :: Systems Administration',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
