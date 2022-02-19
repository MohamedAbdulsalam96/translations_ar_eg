from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in translations_ar_eg/__init__.py
from translations_ar_eg import __version__ as version

setup(
	name="translations_ar_eg",
	version=version,
	description="Custome Arabic Egypt Translation",
	author="Yasser Elbana",
	author_email="yasserelbana@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
