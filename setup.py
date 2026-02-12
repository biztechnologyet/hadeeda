from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

setup(
	name="hadeeda",
	version="0.0.1",
	description="AI-powered Chief of Staff for EthioBiz with autonomous agents, skill management, SOP compliance, and intelligent automation.",
	author="Biz Technology Solutions",
	author_email="support@biztech.et",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires,
)
