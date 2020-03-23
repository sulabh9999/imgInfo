from setuptools import setup, find_packages
import os

thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = thelibFolder + '/requirements.txt'

install_requires = [] 
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()


setup(
	name='imgInfo',
	version='0.1',
	description='Get all info of image in both command line and python API',
	license='Apache',
	author='Sulabh Shukla',
	author_email='sulabh9999@gmail.com',
	packages=find_packages(),
	download_url='https://github.com/sulabh9999/imgInfo',
	maintainer_email='sulabh9999@gmail.com',
	install_requires=install_requires,
	classifiers=[
		'Development Status :: 4 - Beta',
		'Topic :: Software Development :: Build Tools'
	],
	entry_points ={ 
        'console_scripts': [ 
            'imginfo = imgInfo.main:main'
        ] 
    },
    python_requires='>=3.5'
    # packages=['imgInfo']
)