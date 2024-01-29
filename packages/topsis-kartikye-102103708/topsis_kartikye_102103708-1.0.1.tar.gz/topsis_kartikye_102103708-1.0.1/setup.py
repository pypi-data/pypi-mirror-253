import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
  long_description=README,
  long_description_content_type='text/markdown',
  name = 'topsis_kartikye_102103708',       
  version = '1.0.1',     
  license='MIT',      
  description = 'A Python package to find TOPSIS for MCDM (Multi-Criteria Decision Analysis Method)',
  author = 'Kartikye Chadda',
  author_email = 'kartikyechadda@gmail.com',      
  keywords = ['TOPSIS', 'MCDM'],   
  install_requires=[            
          'numpy',
          'pandas',
          'logging',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
  ],
  entry_points={
    'console_scripts': [
      'topsis_kartikye_102103708=topsis:main',
    ],
  },
)