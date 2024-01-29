from setuptools import setup

name = "types-Markdown"
description = "Typing stubs for Markdown"
long_description = '''
## Typing stubs for Markdown

This is a [PEP 561](https://peps.python.org/pep-0561/)
type stub package for the [`Markdown`](https://github.com/Python-Markdown/markdown) package.
It can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
PyCharm, etc. to check code that uses
`Markdown`.

This version of `types-Markdown` aims to provide accurate annotations
for `Markdown==3.5.*`.
The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/Markdown. All fixes for
types and metadata should be contributed there.

This stub package is marked as [partial](https://peps.python.org/pep-0561/#partial-stub-packages).
If you find that annotations are missing, feel free to contribute and help complete them.


See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `fd89040900364a1cd6b6d5be6f65975d50e695a7` and was tested
with mypy 1.8.0, pyright 1.1.342, and
pytype 2023.12.18.
'''.lstrip()

setup(name=name,
      version="3.5.0.20240129",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/Markdown.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['markdown-stubs'],
      package_data={'markdown-stubs': ['__init__.pyi', '__meta__.pyi', 'blockparser.pyi', 'blockprocessors.pyi', 'core.pyi', 'extensions/__init__.pyi', 'extensions/abbr.pyi', 'extensions/admonition.pyi', 'extensions/attr_list.pyi', 'extensions/codehilite.pyi', 'extensions/def_list.pyi', 'extensions/extra.pyi', 'extensions/fenced_code.pyi', 'extensions/footnotes.pyi', 'extensions/legacy_attrs.pyi', 'extensions/legacy_em.pyi', 'extensions/md_in_html.pyi', 'extensions/meta.pyi', 'extensions/nl2br.pyi', 'extensions/sane_lists.pyi', 'extensions/smarty.pyi', 'extensions/tables.pyi', 'extensions/toc.pyi', 'extensions/wikilinks.pyi', 'inlinepatterns.pyi', 'postprocessors.pyi', 'preprocessors.pyi', 'serializers.pyi', 'treeprocessors.pyi', 'util.pyi', 'METADATA.toml', 'py.typed']},
      license="Apache-2.0 license",
      python_requires=">=3.8",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
