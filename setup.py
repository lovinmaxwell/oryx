from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in oryxerp/__init__.py
from oryxerp import __version__ as version

setup(
	name="oryxerp",
	version=version,
	description="Open Source ERP ",
	author="Oryx",
	author_email="lovin@oryxerp.qa",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
