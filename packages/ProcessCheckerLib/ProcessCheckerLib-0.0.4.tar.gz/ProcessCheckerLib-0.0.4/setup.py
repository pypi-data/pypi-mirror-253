from setuptools import setup, find_packages


def readme():
  with open('README.txt', 'r') as f:
    return f.read()


setup(
  name='ProcessCheckerLib',
  version='0.0.4',
  author='Brambleaka',
  author_email='sambuka11jail@outlook.com',
  description='This is lib for work with scripts exceptions.',
  long_description=readme(),
  long_description_content_type='text',
  url='',
  packages=find_packages(),
  install_requires=['requests','psutil','flask','schedule','logging','werkzeug'],
  classifiers=[
    'Programming Language :: Python :: 3.12',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='',
  project_urls={},
  python_requires='>=3.11'
)