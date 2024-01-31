from setuptools import setup, find_packages
from admin_tool_button.version import Version


setup(name='admin_tool_button',
     version=Version('1.0.6-alpha').number,
     description='Extra tool buttons for Django admin',
     long_description=open('README.md').read().strip(),
     long_description_content_type="text/markdown",
     author='Bram Boogaard',
     author_email='padawan@hetnet.nl',
     url='https://github.com/bboogaard/admin_tool_button',
     packages=find_packages(include=['admin_tool_button', 'admin_tool_button.contrib']),
     install_requires=[
         'pytest',
         'pytest-cov',
         'pytest-django==4.5.2',
         'django~=4.2.7'
     ],
     license='MIT License',
     zip_safe=False,
     keywords='Django Admin',
     classifiers=['Development Status :: 3 - Alpha'])
