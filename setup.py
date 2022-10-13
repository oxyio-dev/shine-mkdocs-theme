from setuptools import setup, find_packages

VERSION = '0.3.4'

setup(
  name="mkdocs-shine",
  version=VERSION,
  url='https://github.com/oxyio-dev/shine-mkdocs-theme',
  license='MIT',
  description='Elegant theme for MkDocs c/o Shine',
  author='shine oxyio',
  packages=find_packages(),
  include_package_data=True,
  install_requires=[
    'mkdocs-awesome-pages-plugin'
  ],
  entry_points={
    'mkdocs.themes': [
      'shine = shine_theme',
    ]
  },
  zip_safe=False
)
