from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'A framework for cross-device communication.'
LONG_DESCRIPTION = 'Origin is a configurable, permission-scoped framework for cross-device communication over the internet.'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="pyorigin", 
        version=VERSION,
        author="William Jackson",
        author_email="william@jcksn.io",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that need to be installed along with your package.
        
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Natural Language :: English",
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
            "Topic :: Internet"
        ]
)