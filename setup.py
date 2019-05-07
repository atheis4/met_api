from setuptools import setup

dependencies = [
    'attrdict',
    'bs4',
    'lxml',
    'pandas',
    'requests'
]

setup(
    name='pymet',
    version='0.0.1',
    packages=['pymet'],
    url='https://github.com/atheis4/met_api',
    dependencies=dependencies,
    license='',
    author='Andrew',
    author_email='andrewtheis4@gmail.com',
    description=(
        'Python API for consuming the Metropolitan '
        'Museum of Art\'s open access collection.'
    )
)
