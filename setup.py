from setuptools import setup
setup(
    name = 'ICTLife-CLI',
    version = '0.0.1',
    packages = ['ICTLife-Interview'],
    entry_points = {
        'console_scripts': [
            'ICTLife-Interview = ICTLife-Interview.__main__:main'
        ]
    })
