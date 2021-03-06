# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased](https://github.com/at-gmbh/personio-py/compare/v0.1.1...HEAD)

* add support for new API functions: `get_absences`, `get_attendances`
* add support for paginated API requests (required for attendances & absences)
* make `from_dict()` and `to_dict()` behave consistently
* meta: improve CI builds & tests, better pre-commit hooks

## [0.1.1](https://github.com/at-gmbh/personio-py/tree/v0.1.1) - 2020-08-19

- This is the first release of the Personio API client library
- Created Python module `personio_py`
- Documentation using Sphinx (on [GitHub Pages](https://at-gmbh.github.io/personio-py/))
