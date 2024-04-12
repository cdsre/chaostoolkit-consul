 # Chaos Toolkit Extension for Hashicorp Consul
[![Build Status](https://travis-ci.org/chaostoolkit-incubator/chaostoolkit-istio.svg?branch=master)](https://travis-ci.org/chaostoolkit-incubator/chaostoolkit-istio)
[![Python versions](https://img.shields.io/pypi/pyversions/chaostoolkit-istio.svg)](https://www.python.org/)


This project is a collection of [actions][] and [probes][], gathered as an
extension to the [Chaos Toolkit][chaostoolkit].

[actions]: http://chaostoolkit.org/reference/api/experiment/#action
[probes]: http://chaostoolkit.org/reference/api/experiment/#probe
[chaostoolkit]: http://chaostoolkit.org

## Install

This package requires Python 3.6+

To be used from your experiment, this package must be installed in the Python
environment where [chaostoolkit][] already lives.

```
$ pip install -U chaostoolkit-consul
```

## Usage

There are a collection of examples that will continue to grow as use picks up in the module. These are written as 
individual experiments that can be run with the Chaos Toolkit.

* [KV Example](./examples/kv_example.yaml)

Please explore the code to see existing probes and actions.

## Configuration

This extension needs you specify how to connect to the consul cluster. Please refer to the [consul ENV][consul-env] docs
for more information.

[consul-env]: https://developer.hashicorp.com/consul/commands#environment-variables

### Test

To run the tests for the project execute the following:

```
$ pdm run test
```

### Formatting and Linting

We use a combination of [`black`][black], [`ruff`][ruff], and [`isort`][isort]
to both lint and format this repositories code.

[black]: https://github.com/psf/black
[ruff]: https://github.com/astral-sh/ruff
[isort]: https://github.com/PyCQA/isort

Before raising a Pull Request, we recommend you run formatting against your
code with:

```console
$ pdm run format
```

This will automatically format any code that doesn't adhere to the formatting
standards.

As some things are not picked up by the formatting, we also recommend you run:

```console
$ pdm run lint
```

To ensure that any unused import statements/strings that are too long, etc.
are also picked up.

## Contribute

If you wish to contribute more functions to this package, you are more than
welcome to do so. Please, fork this project, make your changes following the
usual [black][blackstyle] code style, sprinkling with tests and submit a PR for
review.

[blackstyle]: https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html

To contribute to this project, you will also need to install [pdm][].

[pdm]: https://pdm.fming.dev/latest/