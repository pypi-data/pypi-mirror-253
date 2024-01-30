from setuptools import setup, find_packages
 
# classifiers = [
#   'Development Status :: 5 - Production/Stable',
#   'Intended Audience :: Education',
#   'Operating System :: Microsoft :: Windows :: Windows 10',
#   'License :: OSI Approved :: MIT License',
#   'Programming Language :: Python :: 3'
# ]
 
# setup(
#   name=' monitoringdashboard',
#   version='0.8',
#   description='A very basic model monitoring package',
#   url='',  
#   author='Ritik',
#   packages=['monitoringdashboard'],
#   install_requires=['streamlit','pandas','datetime','numpy'] 
# )

from setuptools import setup, find_packages

setup(
    name='monitoringdashboard',
    version='0.8',
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'pandas',
        # Add any other dependencies
    ],
)