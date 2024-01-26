# cici-tools

<!-- BADGIE TIME -->

[![brettops tool](https://img.shields.io/badge/brettops-tool-209cdf?labelColor=162d50)](https://brettops.io)
[![pipeline status](https://img.shields.io/gitlab/pipeline-status/brettops/tools/cici-tools?branch=main)](https://gitlab.com/brettops/tools/cici-tools/-/commits/main)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![code style: black](https://img.shields.io/badge/code_style-black-000000.svg)](https://github.com/psf/black)
[![imports: isort](https://img.shields.io/badge/imports-isort-1674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg)](https://github.com/prettier/prettier)

<!-- END BADGIE TIME -->

> **WARNING:** `cici` is experimental and I can't even decide on a name for it.
> Stay away!

## Usage

### `bundle`

Flatten `extends` keywords to make zero-dependency GitLab CI/CD files.

```bash
cici bundle
```

```console
$ cici bundle
pipeline name: python
bundle names: ['black', 'isort', 'mypy', 'pyroma', 'pytest', 'setuptools', 'twine', 'vulture']
created black.yml
created isort.yml
created mypy.yml
created pyroma.yml
created pytest.yml
created setuptools.yml
created twine.yml
created vulture.yml
```

```yaml
include:
  - project: brettops/pipelines/python
    ref: ""
    file:
      - black.yml
      - isort.yml
      - vulture.yml
```

### `fmt`

Normalize the style of your GitLab CI/CD files:

```bash
cici fmt
```

```console
$ cici fmt
.gitlab-ci.yml formatted
```

### `update`

Update to the latest GitLab CI/CD `include` versions available.

```bash
cici update
```

```console
$ cici update
brettops/pipelines/prettier has no releases
brettops/pipelines/python is the latest at 0.5.0
```
