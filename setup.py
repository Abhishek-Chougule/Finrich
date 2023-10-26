from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in finrich/__init__.py
from finrich import __version__ as version

setup(
	name="finrich",
	version=version,
	description="Financial Data Gethering",
	author="Abhishek Chougule",
	author_email="abhishek.c@onehash.ai",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
