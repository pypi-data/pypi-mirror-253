# Development

**Please develop inside the container**, this will ensure all the required checks (`pylint` & `mypy`) as well as formatting (`black`)

If you are not familiar with devcontainers, read [Developing inside a Container](https://code.visualstudio.com/docs/devcontainers/containers) first

1. Clone this repository
2. open dir in *VS Code* `vscode .`
3. rebuild and reopen in container (you'll need `Dev Containers` extension)

**note**: if a container with `devcontainer` name already exists, an error will occur. You can remove it with
`docker container prune -f`


### What goes where

* `gitlab-ci.yml` - gitlab ci script
* `init_container.sh` script to initialize container for development.
* `setup.py` - main packge setup file
* `docs` - documentation, uses mkdocs
* `install` - scripts for preparing host system

### Version control

Version control is done with git tags using `setuptools_scm`

use `git tag v1.2.3` to update version number. Use `git describe` to show current version.

### Documentation

The documentation is automatically generated from the content of the [docs directory](./docs) and from the docstrings
 of the public signatures of the source code.

run `serve_docs.sh` from inside the container to build and serve documentation.

**note:** `pyreverse` creates images of packages and classes in `docs/uml/..`

### Pre-commit

optional. Add `precommit install` to `init_container.sh` if required.

