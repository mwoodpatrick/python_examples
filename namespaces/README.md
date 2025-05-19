# Namespaces

This repository contains code related to the Real Python tutorial [How to Use Loguru for Simpler Python Logging](https://realpython.com/python-loguru/).

## Setup environment

You should first create and activate a virtual environment:

```sh
$ nix-shell
$ python -m venv venv/
$ source venv/bin/activate
```

Install the pinned dependencies from `requirements.txt`:

```sh
(venv) $ python -m pip install -r requirements.txt
```

Then you can execute the provided Python scripts, for example:

```sh
(venv) $ python basic_logging.py
```

## Rendering Docs

To convert the README.md to html use:

```sh
pandoc README.md -o README.html
```

To display the generated html file use:

```sh
firefox README.html &
```


## References

1. [click](https://docs.google.com/document/d/1uzLWBVaI9EotwqOt-521bBM5jlpLCbH55fc70lWBK7k/edit?pli=1&tab=t.0)
1. [Using pip and pyproject.toml](https://gemini.google.com/share/ca70de5996e0)
1. [import click using pyproject.toml](https://docs.google.com/document/d/1cejOZYgWVBocAskS2ziipkA71OpUXNscpYaFQ7vdzSE/edit?tab=t.0)
1. [Namespaces](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces)
2. [Import](https://docs.python.org/3/reference/simple_stmts.html#import)
3. [The import system](https://docs.python.org/3/reference/import.html)
4. [What is __init__.py file in Python](https://www.python-engineer.com/posts/init-py-file/)
5. [pyproject.toml](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/)
6. [TOML - Syntax](https://www.w3schools.io/file/toml-syntax/)
6. [adding comments to toml file](https://www.bing.com/search?q=adding+comments+to+toml+file&form=ANNTH1&refig=31e13b1ad81f4cd59b25e1f8b0b54662&pc=W147&ucpdpc=UCPD&adppc=EDGEDBB)
5. [PEP 518 – Specifying Minimum Build System Requirements for Python Projects](https://peps.python.org/pep-0518/)
5. [pep 518 python](https://www.bing.com/search?q=pep+518+python&FORM=QSRE1)
5. [Clarifying PEP 518 (a.k.a. pyproject.toml)](https://snarky.ca/clarifying-pep-518/)
5. [Good packaging/setuptools/whatever tutorial?](https://discuss.python.org/t/good-packaging-setuptools-whatever-tutorial/19378/3)
6. [ItsUtils](https://github.com/TheItsProjects/ItsUtils)
5. [Python](https://nixos.wiki/wiki/Python)
6. [Python Enhancement Proposals (PEPs): A Comprehensive Guide](https://coderivers.org/blog/pep-python/)
6. [Markdown Guide](https://www.markdownguide.org/)
7. [Tools To Convert PDF Files to Markdown](https://pdf.wondershare.com/convert-pdf/pdf-to-markdown.html)
8. [Releasing your package](https://pythonpackaging.info/07-Package-Release.html)
