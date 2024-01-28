from setuptools import setup, find_packages

with open("README.md", "r") as f:
  description = f.read()


setup(
  name='PyEDCR',
  version='0.1.11',
  author='Joshua Shay Kricheli, Paulo Shakarian, Spencer Ozgur, Aniruddha Datta, Khoa Vo',
  author_email='name@example.com',
  description='A short description of your package',
  packages=find_packages(),
  classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
  ],
  python_requires='>=3.6',
  long_description=description,
  long_description_content_type = "text/markdown",
  install_requires=[line.strip() for line in open("src/requirements.txt").readlines()],
  include_package_data=True
)
