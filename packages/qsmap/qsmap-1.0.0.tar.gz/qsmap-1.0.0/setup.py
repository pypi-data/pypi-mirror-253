import setuptools

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name = 'qsmap', 
    packages = ['qsmap'],
    version='1.0.0',
    author='Yaroslav Mavliutov',
    author_email='yaroslavm@questarauto.com',
    description = 'Package provides functionality for working with geographical data, routing, and mapping',
    url='https://github.com/saferide-tech/QuestarMap',
    license='MIT',
    keywords = ['geo', 'routing', 'mapping'],
    install_requires=requirements,
)