import setup from setuptools
setup(
    name = 'ICTLife-CLI',
    version = '0.0.1',
    packages = ['ICTLifeInterview'],
    entry_points = {
        'console_scripts': [
            'ICTLifeInterview = ICTLifeInterview.__main__:main'
        ]
    })
