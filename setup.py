#####################
# IMPORTS
#####################
from setuptools import setup, find_packages

#####################
# SETUP
#####################
def dependencies(imported_file):
    with open(imported_file) as file:
        return file.read().splitlines()

with open("README.md") as file:
    # PROVISION
    setup(
        name="demo",
        url="https://jakob.pennington.io",
        author="Jakob Pennington",
        author_email="jakob@pennington.io",
        version='1.0.0',
        description="Runs sslscan as a demo for Kali development containers.",
        packages=find_packages(),
        entry_points={'console_scripts': ['demo = demo.demo:main']}
    )
