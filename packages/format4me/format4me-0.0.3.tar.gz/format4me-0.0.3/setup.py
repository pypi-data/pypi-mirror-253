from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='format4me',
  version='0.0.3',
  description='A library to easily format the response coming from your bard or any other ai agent .',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Sahil Pradhan',
  author_email='sahilpradhan411@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['responseFormatter','chatgpt','bard'], 
  packages=find_packages(),
  install_requires=['regex'] 
)
