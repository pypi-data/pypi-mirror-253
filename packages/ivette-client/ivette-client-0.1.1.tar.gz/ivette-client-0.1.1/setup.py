from setuptools import setup

setup(
    name='ivette-client',
    version='0.1.1',
    description='Python client for Ivette Computational chemistry and Bioinformatics project',
    author='Eduardo Bogado',
    py_modules=['run_ivette',
                'ivette',
                'ivette.classes',
                'ivette.decorators',
                'ivette.newtworking',
                'ivette.processing',
                'ivette.types',
                'ivette.utils'],
    entry_points={
        'console_scripts': [
            'ivette-client=run_ivette:main',
        ],
    },
)
