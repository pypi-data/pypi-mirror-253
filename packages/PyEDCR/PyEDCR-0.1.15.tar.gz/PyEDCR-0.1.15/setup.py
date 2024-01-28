import setuptools

with open("README.md", "r", encoding="utf-8") as f:
  description = f.read()


setuptools.setup(
  name='PyEDCR',
  version='0.1.15',
  author='Joshua Shay Kricheli, Paulo Shakarian, Spencer Ozgur, Aniruddha Datta, Khoa Vo',
  author_email='name@example.com',
  description='A short description of your package',
  classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
  ],
  python_requires='>=3.7',
  long_description=description,
  long_description_content_type = "text/markdown",
  package_dir={"": "src"},
  packages=setuptools.find_packages(where="src"),
)
