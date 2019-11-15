from setuptools import setup, find_packages

setup(
    name='neo4j-manager',
    version='1.0',
    description='manage multiple neo4j databases',
    url='',
    author='Simon Koch',
    author_email='projects@halcony.de',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    scripts=['src/neo4j-manager'],
    zip_safe=False,
    license='GPLv3')
