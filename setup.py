from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in practice_app/__init__.py
from practice_app import __version__ as version

setup(
	name="practice_app",
	version=version,
	description="NA",
	author="Yatharth",
	author_email="letstalk.yatharth@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
