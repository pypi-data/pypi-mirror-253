# SPDX-License-Identifier: MIT OR Apache-2.0
# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the MIT License.  See the LICENSE file in the root of this
# repository for complete details.
# Python imports
import os
import sys


sys.path.insert(0, os.path.abspath(".."))
# Internal imports
from tools.versioning import get_version


# We want an image in the README and include the README in the docs.
suppress_warnings = ["image.nonlocal_uri"]


# -- General configuration ----------------------------------------------------

extensions = [
    "myst_parser",
    "notfound.extension",
    "sphinx.ext.autodoc",
    "sphinx.ext.autodoc.typehints",
    "sphinx.ext.napoleon",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinxcontrib.mermaid",
    "sphinxext.opengraph",
]

myst_enable_extensions = [
    "colon_fence",
    "smartquotes",
    "deflist",
]
mermaid_init_js = "mermaid.initialize({startOnLoad:true,theme:'neutral'});"

# ogp_image = "_static/pymox_logo.png"


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = [".rst", ".md"]

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "pymox"
author = "Ivan Neto"
copyright = f"2023, { author }"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# The full version, including alpha/beta/rc tags.
release = get_version()
print("RELEASE:")
print(release)
# release = metadata.version("pymox")
# The short X.Y version.
version = release.rsplit(".", 1)[0]

if "dev" in release:
    release = version = "UNRELEASED"

exclude_patterns = ["_build"]

# The reST default role (used for this markup: `text`) to use for all
# documents.
default_role = "any"

nitpick_ignore = []

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# Move type hints into the description block, instead of the func definition.
autodoc_typehints = "description"
autodoc_typehints_description_target = "documented"

# -- Options for HTML output --------------------------------------------------

html_theme = "furo"
html_theme_options = {
    "top_of_page_button": None,
    "light_css_variables": {
        "font-stack": "Inter, sans-serif",
        "font-stack--monospace": "BerkeleyMono, MonoLisa, ui-monospace, "
        "SFMono-Regular, Menlo, Consolas, Liberation Mono, monospace",
    },
}
# html_logo = "_static/pymox_logo.svg"
html_static_path = ["_static"]
# html_css_files = ["custom.css"]

htmlhelp_basename = "pymoxdoc"

latex_documents = [
    (master_doc, "pymox.tex", "pymox Documentation", f"{author}", "manual"),
]

# -- Options for manual page output -------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "pymox", "pymox Documentation", [author], 1)]


# -- Options for Texinfo output -----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, "pymox", "pymox Documentation", author, "pymox", "One line description of project.", "Miscellaneous"),
]


# -- Options for Epub output --------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# GitHub has rate limits
linkcheck_ignore = [
    r"https://github.com/.*/(issues|pull|compare)/\d+",
    r"https://twitter.com/.*",
]

# Twisted's trac tends to be slow
linkcheck_timeout = 300

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "rich": ("https://rich.readthedocs.io/en/stable/", None),
}
