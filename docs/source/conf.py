# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import os
from os import path as pth
import sys

# No idea which one of these is the right one for RTD, but now it works,
# so don't touch them!
sys.path.insert(0, os.path.abspath('/'))
sys.path.insert(0, os.path.abspath('docs'))
sys.path.insert(0, os.path.abspath('docs/source/'))

sphinx_ext_path = pth.join(pth.abspath(pth.dirname(__file__)), "_ext")
sys.path.append(sphinx_ext_path)

package_path = pth.abspath('../..')
os.environ['PYTHONPATH'] = ';'.join((package_path,
                                     sphinx_ext_path,
                                     os.environ.get('PYTHONPATH', '')))

# -- Project information -----------------------------------------------------

project = 'ScopeSim'
copyright = '2019, A*Vienna'
author = 'Kieran Leschinski, Oliver Czoske'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'scopesim_sphinx_ext',
    'nbsphinx',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'numpydoc',
    'matplotlib.sphinxext.plot_directive',
    'sphinxcontrib.apidoc',
    'sphinx.ext.autodoc',

    # 'jupyter_sphinx.execute',
    # 'sphinx.ext.coverage',
]

# apidoc settings
numpydoc_show_class_members = False
apidoc_module_dir = pth.abspath('../../scopesim/')
apidoc_output_dir = 'reference'
apidoc_separate_modules = True
apidoc_excluded_paths = ["tests/", "docs/"]

# Matplotlib plot directive config parameters
plot_html_show_source_link = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
if not os.environ.get("READTHEDOCS") == "True":
    import sphinx_rtd_theme
    html_theme = "sphinx_rtd_theme"
    extensions += ["sphinx_rtd_theme"]
    os.environ["PYTHONPATH"] += "F:\\Work\\ScopeSim;F:\\Work\\HowManyBloodyPhotons;F:\\Work\\ScopeSim_Templates;F:\\Work\\Pyckles;F:\\Work\\AnisoCADO;F:\\Work\\skycalc_ipy;F:\\Work\\speXtra;"

nbsphinx_execute = "never"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_favicon = '_static/logos/S_favicon.png'


# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'ScopeSimDocs'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'ScopeSim.tex', 'ScopeSim Documentation',
     'Kieran Leschinski', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'scopesim', 'ScopeSim Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'ScopeSim', 'ScopeSim Documentation',
     author, 'ScopeSim', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'python': ('http://docs.python.org/', None),
                       'numpy': ('http://docs.scipy.org/doc/numpy/', None),
                       'scipy': ('http://docs.scipy.org/doc/scipy/reference/', None),
                       'matplotlib': ('http://matplotlib.org/', None),
                       'astropy': ('http://docs.astropy.org/en/stable/', None),
                       'synphot': ('https://synphot.readthedocs.io/en/latest/', None),
                       'scopesim_templates': ('https://scopesim_templates.readthedocs.io/en/latest/', None),
                       'pyckles': ('https://pyckles.readthedocs.io/en/latest/', None),
                       'anisocado': ('https://anisocado.readthedocs.io/en/latest/', None),
                       }


# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
