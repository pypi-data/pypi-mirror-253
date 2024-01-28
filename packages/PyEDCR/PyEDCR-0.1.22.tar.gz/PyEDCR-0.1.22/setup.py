import setuptools

with open("README.md", "r", encoding="utf-8") as f:
  description = f.read()


setuptools.setup(
  name='PyEDCR',
  version='0.1.22',
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
  install_requires=[           
    'beautifulsoup4',
    'LTNtorch',
    'matplotlib',
    'numpy',
    'opencv_python',
    'pandas',
    'Pillow',
    'protobuf',
    'Requests',
    'scikit_learn',
    'timm',
    'torch',
    'torchsummary',
    'torchvision',
    'tqdm'
  ],
  package_data={
      'src.metacognitive_error_detection_and_correction_v2.combined_results': [
          'vit_b_16_BCE_test_coarse_pred_lr0.0001_e19.npy', 
          'vit_b_16_BCE_test_fine_pred_lr0.0001_e19.npy',
      ],
      'src.metacognitive_error_detection_and_correction_v2.test_fine': [
          "src/metacognitive_error_detection_and_correction_v2/test_fine/test_true_fine.npy",
      ],
  },
)