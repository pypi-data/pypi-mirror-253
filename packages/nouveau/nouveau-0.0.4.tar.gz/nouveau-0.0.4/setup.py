from setuptools import setup,find_packages
from os import path

with open('README.md') as f:
    long_description = f.read()

name = 'nouveau'
version = '0.0.4'

from shutil import copyfile
_workdir = path.abspath(path.dirname(__file__))
copyfile(_workdir+'/README.md',_workdir+'/nouveau/__doc__'.format(name))

setup(name=name
    , version=version
    , description='public domain art nouveau image data'
    , long_description=long_description
    , long_description_content_type='text/markdown'
    , url='https://github.com/dactylroot/{}'.format(name) # source URL
    , download_url="https://github.com/dactylroot/{0}/archive/{1}.tar.gz".format(name,version)
    , license='Unlicense'
    , packages=find_packages()
    , include_package_data=True     # includes files from e.g. MANIFEST.in
    , classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: The Unlicense (Unlicense)',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
      ]
    , keywords=['art','data','dataset']
    , install_requires=['pandas','numpy','pillow','scikit-learn']
    , python_requires='>=3.5'
    , zip_safe=True
     )


