from setuptools import setup
from setuptools.command.install import install
import subprocess
import sys


class CustomStemInstallCommand(install):
    def run(self):
        r"""
        Install packages STEM Application and KratosMultiphysics
        """
        subprocess.check_call([sys.executable, "-m", "pip", "install", "git+https://github.com/StemVibrations/gmsh_utils"])
        subprocess.check_call([sys.executable, "-m", "pip", "install", "git+https://github.com/StemVibrations/RandomFields"])

        # Call the default install process
        install.run(self)


if __name__ == '__main__':
    setup(
        cmdclass={
            'install': CustomStemInstallCommand,
    })
