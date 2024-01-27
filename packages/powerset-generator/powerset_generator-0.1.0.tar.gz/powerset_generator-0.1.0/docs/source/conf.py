# There has to be a better way
import os
import sys
import tomllib

from powerset_generator import __about__

sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("../../src"))

# Pull general sphinx project info from pyproject.toml
with open("../../pyproject.toml", "rb") as f:
    toml = tomllib.load(f)

version = __about__.__version__

pyproject = toml["project"]

project = pyproject["name"]
release = version
author = ",".join([author["name"] for author in pyproject["authors"]])
copyright = f"2024 {author}"

rst_prolog = f"""
.. |project| replace:: **{project}**
.. |root| replace:: :mod:`powerset_generator`
"""


extensions: list[str] = [
    "sphinx.ext.autodoc",
    "sphinx_autodoc_typehints",
    "sphinx.ext.doctest",
]

### doctest setup
doctest_global_setup = """
from powerset_generator import subsets
"""


extensions.append("sphinx.ext.intersphinx")
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

extensions.append("sphinx.ext.mathjax")

templates_path = ["_templates"]
exclude_patterns: list[str] = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
