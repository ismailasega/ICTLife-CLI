from setuptools import setup
setup(
    name = 'ICTLife-CLI',
    version = '1.0',
    packages = ['ICTLifeInterview'],
    entry_points = {
        'console_scripts': [
            'ICTLifeInterview = ICTLifeInterview.__main__:main'
        ]
    })
