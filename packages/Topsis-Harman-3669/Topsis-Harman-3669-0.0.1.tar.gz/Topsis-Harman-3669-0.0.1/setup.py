from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 11',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='Topsis-Harman-3669',
  version='0.0.1',
  description='Topsis Score Calculator',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Harmanpreet Singh',
  author_email='josh@edublocks.org',
  license='MIT', 
  classifiers=classifiers,
  keywords='Topsis', 
  packages=find_packages(),
  install_requires=['numpy','pandas']
)