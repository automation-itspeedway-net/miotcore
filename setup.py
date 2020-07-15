## Modular Home Automation - Core Modules
## (c) Copyright Si Dunford, 2019

import setuptools
from setuptools.command.install import install

VERSION_NUMBER = '1.0.3.3'
VERSION_STATUS = 'Development Status :: 2 - Pre-Alpha'

#Development Status :: 1 - Planning
#Development Status :: 2 - Pre-Alpha
#Development Status :: 3 - Alpha
#Development Status :: 4 - Beta
#Development Status :: 5 - Production/Stable
#Development Status :: 6 - Mature
#Development Status :: 7 - Inactive  

with open("README.md", "r") as fh:
    long_description = fh.read()
       
class CustomInstaller(install):
    def run(self):
        import os,sys
        
        print( "Installing MIOT core modules" )
        # Pre-Install
        
        # Install
        install.run(self)
        
        # Post-Install
        print( "- Platform: "+sys.platform )
        #if sys.platform in ['darwin', 'linux']:
        #    os.system('./linux_installer.sh')

setuptools.setup(
    name='miot',  
    version=VERSION_NUMBER,
    author="Si Dunford",
    author_email="dunford.sj+miot@gmail.com",
    description="Modular Internet of Things, Core modules",
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/automation-itspeedway-net/miotcore.git",
    packages=setuptools.find_packages(),
    classifiers=[
        VERSION_STATUS,
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Other Audience",
        "Topic :: Scientific/Engineering :: Human Machine Interfaces"
        ],
    install_requires=[
        'paho-mqtt',
        'configparser'
        ],
    include_package_data=True,
    python_requires='>=3.6',
    scripts=['bin/miotrepl'],
    cmdclass={
        'install':CustomInstaller
        }
)

