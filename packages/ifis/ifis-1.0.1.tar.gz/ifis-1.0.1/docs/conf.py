# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys

sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'IFIS library'
copyright = '2023, Piotr Grochowalski, Dawid Kosior, Dorota Gil, Wojciech Kozioł, Barbara Pękala, Krzysztof Dyczkowski, Uzay Kaymak, Caro Fuchs, Marco S. Nobile'
author = 'Piotr Grochowalski, Dawid Kosior, Dorota Gil, Wojciech Kozioł, Barbara Pękala, Krzysztof Dyczkowski, Uzay Kaymak, Caro Fuchs, Marco S. Nobile'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = [
    'myst_parser',

    'sphinx.ext.autosectionlabel',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    #'sphinx.ext.duration',
    'sphinx.ext.extlinks',
    'sphinx.ext.githubpages',
    'sphinx.ext.graphviz',
    'sphinx.ext.ifconfig',
    'sphinx.ext.imgconverter',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.intersphinx',
    # 'sphinx.ext.linkcode',

 #   'sphinx.ext.autosummary',
    #'numpydoc',
    #         'rinoh.frontend.sphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo'
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme_github_versions'
html_static_path = ['_static']

# EPUB options
epub_show_urls = 'footnote'
