from setuptools import setup, find_packages
import os
import sys

# Check existence of version file
current_version_path = "./version.txt"
if not os.path.exists(current_version_path):
    raise Exception("Version file missing")


# Reading version and parsing it
try:
    f = open(current_version_path, 'r')
    versions = f.read().split('.')
    f.close()

    major_version = int(versions[0])
    minor_version = int(versions[1])
    patch_version = int(versions[2])
except:
    raise Exception("Error in determining existing version of package")


# Depending on parameter, 
if len(sys.argv) < 4: raise Exception("No version update specified, should be major, minor or patch")
if sys.argv[3] == "major": major_version += 1    
if sys.argv[3] == "minor": minor_version += 1   
if sys.argv[3] == "patch": patch_version += 1   
sys.argv = sys.argv[0:3] # Removing last added CLI argument


# Version
new_version = f"{major_version}.{minor_version}.{patch_version}"


# Setup the package
setup(
    name="geovdata",
    version=new_version,
    author='Gaétan Muck',
    author_email='gaetan.muck@kleiolab.com',
    description='Package with various python tools',
    long_description='Package with various python tools created to help analysis on Geovistory and other SPARQL endpoints.',
    packages=find_packages(),
    install_require=[
    ],
    keywords=['python', 'toolkit', 'utilities', 'utils', 'tools', 'sparql']
)


# Save locally the version number
f = open(current_version_path, 'w')
f.write(new_version)
f.close()