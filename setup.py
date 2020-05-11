from setuptools import setup #import setup function from the python setuptools Package
setup(
    name = 'ICTLife-CLI', #Project/Interview name
    version = '1.0', #Application Version
    packages = ['ICTLifeInterview'], #Application Package
    entry_points = {
        'console_scripts': [
            'ICTLifeInterview = ICTLifeInterview.__main__:main'
        ] #The application runnable is ICTLifeInterview, and when executed will 
        #run the main function in the __main__ module which is part of the
        #ICTLifeInterview package
    })
