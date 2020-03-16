from setuptools import setup, find_packages

setup(
	name='imgInfo',
	version='1.0',
	description='get all info of given image in both command line and python API',
	license='Apache',
	author='Sulabh Shukla',
	author_email='sulabh9999@gmail.com',
	packages=find_packages(),
	download_url='https://github.com/sulabh9999',
	maintainer_email='sulabh9999@gmail.com',
	install_requires=['Pillow'],
	classifiers=[
		'Development Status :: Alpha',
		'Operating Sysytem :: ubuntu 18.04',
		'Topic :: Software Development :: Build Tools',
		'Programming Language :: Python :: 3.6',
	],
	scripts=["imgInfo.py"]
)