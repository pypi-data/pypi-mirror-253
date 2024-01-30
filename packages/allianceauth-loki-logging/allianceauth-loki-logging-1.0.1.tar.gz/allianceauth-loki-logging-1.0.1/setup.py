import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

#from allianceauth_loki_logging import __version__

__version__ = "1.0.1"

setup(
    name='allianceauth-loki-logging',
    version=__version__,
    packages=find_packages(),
    url='https://github.com/Solar-Helix-Independent-Transport/allianceauth-loki-logging',
    license='MIT',
    author='aaronkable',
    author_email='aaronkable@gmail.com',
    description='A non-blocking django logging handler for Loki',
    long_description=README,
    long_description_content_type="text/markdown",
    keywords=['python', 'loki', 'grafana', 'logging', 'metrics', 'threaded'],
    install_requires=[
        'requests',
        'pytz',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        "Environment :: Web Environment",
        'Framework :: Django',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
