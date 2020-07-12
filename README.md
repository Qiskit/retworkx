# retworkx

[![License](https://img.shields.io/github/license/Qiskit/retworkx.svg?style=popout-square)](https://opensource.org/licenses/Apache-2.0)
[![Build Status](https://img.shields.io/travis/com/Qiskit/retworkx/master.svg?style=popout-square)](https://travis-ci.com/Qiskit/retworkx)
[![](https://img.shields.io/github/release/Qiskit/retworkx.svg?style=popout-square)](https://github.com/Qiskit/retworkx/releases)
[![](https://img.shields.io/pypi/dm/retworkx.svg?style=popout-square)](https://pypi.org/project/retworkx/)
[![Coverage Status](https://coveralls.io/repos/github/Qiskit/retworkx/badge.svg?branch=master)](https://coveralls.io/github/Qiskit/retworkx?branch=master)
[![Minimum rustc 1.39](https://img.shields.io/badge/rustc-1.39+-blue.svg)](https://rust-lang.github.io/rfcs/2495-min-rust-version.html)

  - You can see the full rendered docs at:
    <https://retworkx.readthedocs.io/en/latest/index.html>

retworkx is a general purpose graph library for python3 written in Rust to
take advantage of the performance and safety that Rust provides. It was built
as a replacement for [qiskit](https://qiskit.org/)'s previous (and current)
networkx usage (hence the name) but is designed to provide a high
performance general purpose graph library for any python application. The
project was originally started to build a faster directed graph to use as the
underlying data structure for the DAG at the center of
[qiskit-terra](https://github.com/Qiskit/qiskit-terra/)'s transpiler, but it
has since grown to cover all the graph usage in Qiskit and other applications.

## Installing retworkx

retworkx is published on pypi so on x86\_64, i686, ppc64le, s390x, and
aarch64 Linux systems, x86\_64 on Mac OSX, and 32 and 64 bit Windows
installing is as simple as running:

```bash
pip install retworkx
```

This will install a precompiled version of retworkx into your python
environment.

### Installing on a platform without precompiled binaries

If there are no precompiled binaries published for your system you'll have to
build the package from source for your system. A source package is also
published on pypi, so you still can also run the above `pip` command to install
it. However, to be able able to build the package from the published source
package you need to have rust >=1.39 installed (and also
[cargo](https://doc.rust-lang.org/cargo/) which is normally included with rust)
You can use [rustup](https://rustup.rs/) (a cross platform installer for rust)
to make this simpler, or rely on
[other installation methods](https://forge.rust-lang.org/infra/other-installation-methods.html).
Once you have rust properly installed, running:

```bash
pip install retworkx
```

will build retworkx for your local system from the source package and install
it just as it would if there was a prebuilt binary available.

## Building from source

The first step for building retworkx from source is to clone it locally
with:

```bash
git clone https://github.com/Qiskit/retworkx.git
```

retworkx uses [PyO3](https://github.com/pyo3/pyo3) and
[setuptools-rust](https://github.com/PyO3/setuptools-rust) to build the
python interface. Which enables using standard python tooling to work. So,
assuming you have rust installed then you can easily install retworkx into your
python environment using `pip`. Once you have a local clone of the repo, change
your current working directory to the root of the repo. Then, you can install
retworkx into your python env with:

```bash
pip install .
```

Assuming your current working directory is still the root of the repo.
Otherwise you can run:

```bash
pip install $PATH_TO_REPO_ROOT
```

which will install it the same way. Then retworkx is installed in your
local python environment. There are 2 things to note when doing this
though, first if you try to run python from the repo root using this
method it will not work as you expect. There is a name conflict in the
repo root because of the local python package shim used in building the
package. Simply run your python scripts or programs using retworkx
outside of the repo root. The second issue is that any local changes you
make to the rust code will not be reflected live in your python environment,
you'll need to recompile retworkx by rerunning `pip install` to have any
changes reflected in your python environment.

## Using retworkx

Once you have retworkx installed you can use it by importing retworkx.
All the functions and graph classes are off the root of the package.
For example, building a DAG and adding 2 nodes with an edge between them
would be:

```python3
import retworkx

my_dag = retworkx.PyDAG(cycle_check=True)
# add_node(), add_child(), and add_parent() return the node index
# The sole argument here can be any python object
root_node = my_dag.add_node("MyRoot")
# The second and third arguments can be any python object
my_dag.add_child(root_node, "AChild", ["EdgeData"])
```
