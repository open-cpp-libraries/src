import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join('..', '..')))

project = 'My Python Project'
author = 'Amlal El Mahrouss'
copyright = '2026, Amlal El Mahrouss'
version = '1.63'
release = '1.63.7'
extensions = ['sphinx.ext.markdown', 'sphinx.ext.napoleon', 'sphinx.ext.viewcode']
language = 'en'
html_theme = 'pydata_sphinx_theme'