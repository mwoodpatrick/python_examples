# How to Use Loguru for Simpler Python Logging

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

1. [How to Use Loguru for Simpler Python Logging](https://realpython.com/python-loguru/)
2. [Loguru](https://loguru.readthedocs.io/en/stable/index.html)
3. [Python](https://nixos.wiki/wiki/Python)
4. [Markdown Guide](https://www.markdownguide.org/)
