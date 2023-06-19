# python_poetry_package

Just a python template package with poetry.


## Development

To install the package and run tests directly from the repository, `poetry` is suggested:
```
git clone https://github.com/Davidelanz/python_poetry_package.git
poetry install
poetry run pytest .
```

> If `poetry install` takes too much time, one can try to:
> - update poetry via `pip install --upgrade poetry`
> - retrieve the cache list via `poetry cache list` and then use `poetry cache clear --all <cache_name>` to delete the cache for `<cache_name>`
