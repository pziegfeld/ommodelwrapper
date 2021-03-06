#
# This file is autogenerated during plugin quickstart and overwritten during
# plugin makedist. DO NOT CHANGE IT if you plan to use plugin makedist to update 
# the distribution.
#

from setuptools import setup, find_packages

kwargs = {'author': 'Kyungjin Moon',
 'author_email': 'kyungjin.moon@asdl.gatech.edu',
 'classifiers': ['Intended Audience :: Science/Research',
                 'Topic :: Scientific/Engineering'],
 'description': 'OpenMDAO Component plugin for wrapping OpenModelica model',
 'download_url': '',
 'entry_points': '[openmdao.container]\nommodelwrapper.ommodelwrapper.OMModelWrapper=ommodelwrapper.ommodelwrapper:OMModelWrapper\n\n[openmdao.component]\nommodelwrapper.ommodelwrapper.OMModelWrapper=ommodelwrapper.ommodelwrapper:OMModelWrapper',
 'include_package_data': True,
 'install_requires': ['openmdao.main'],
 'keywords': ['openmdao'],
 'license': '',
 'maintainer': 'Kyungjin Moon',
 'maintainer_email': '',
 'name': 'ommodelwrapper',
 'package_data': {'ommodelwrapper': ['sphinx_build\\html\\.buildinfo',
                                     'sphinx_build\\html\\genindex.html',
                                     'sphinx_build\\html\\index.html',
                                     'sphinx_build\\html\\objects.inv',
                                     'sphinx_build\\html\\pkgdocs.html',
                                     'sphinx_build\\html\\py-modindex.html',
                                     'sphinx_build\\html\\search.html',
                                     'sphinx_build\\html\\searchindex.js',
                                     'sphinx_build\\html\\srcdocs.html',
                                     'sphinx_build\\html\\usage.html',
                                     'sphinx_build\\html\\_modules\\index.html',
                                     'sphinx_build\\html\\_modules\\ommodelwrapper\\load_modelica_mat.html',
                                     'sphinx_build\\html\\_modules\\ommodelwrapper\\ommodelwrapper.html',
                                     'sphinx_build\\html\\_modules\\ommodelwrapper\\OM_build.html',
                                     'sphinx_build\\html\\_sources\\index.txt',
                                     'sphinx_build\\html\\_sources\\pkgdocs.txt',
                                     'sphinx_build\\html\\_sources\\srcdocs.txt',
                                     'sphinx_build\\html\\_sources\\usage.txt',
                                     'sphinx_build\\html\\_static\\basic.css',
                                     'sphinx_build\\html\\_static\\default.css',
                                     'sphinx_build\\html\\_static\\doctools.js',
                                     'sphinx_build\\html\\_static\\file.png',
                                     'sphinx_build\\html\\_static\\jquery.js',
                                     'sphinx_build\\html\\_static\\minus.png',
                                     'sphinx_build\\html\\_static\\plus.png',
                                     'sphinx_build\\html\\_static\\pygments.css',
                                     'sphinx_build\\html\\_static\\searchtools.js',
                                     'sphinx_build\\html\\_static\\sidebar.js',
                                     'sphinx_build\\html\\_static\\underscore.js',
                                     'test\\openmdao_log.txt',
                                     'test\\SimAcceleration.c',
                                     'test\\SimAcceleration.exe',
                                     'test\\SimAcceleration.makefile',
                                     'test\\SimAcceleration.mo',
                                     'test\\SimAcceleration.o',
                                     'test\\SimAcceleration_functions.c',
                                     'test\\SimAcceleration_functions.h',
                                     'test\\SimAcceleration_init.xml',
                                     'test\\SimAcceleration_records.c',
                                     'test\\SimAcceleration_records.o',
                                     'test\\SimAcceleration_res.mat',
                                     'test\\test_ommodelwrapper.py',
                                     'test\\VehicleDesign.mo',
                                     'test\\_SimAcceleration.h']},
 'package_dir': {'': 'src'},
 'packages': ['ommodelwrapper'],
 'url': '',
 'version': '0.1',
 'zip_safe': False}


setup(**kwargs)

