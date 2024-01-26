
<h1 align=center>
  
  **grepenv**
  
</h1>

<h3 align=center>

  greps your env 🔎

</h3>


<div align=center>

  [![PyPI version](https://badge.fury.io/py/grepenv.svg)](https://badge.fury.io/py/grepenv)
  [![Coverage Status](https://coveralls.io/repos/github/mdLafrance/grepenv/badge.svg?branch=main)](https://coveralls.io/github/mdLafrance/grepenv?branch=main)
  [![Pipeline](https://github.com/mdLafrance/grepenv/actions/workflows/pipeline.yaml/badge.svg)](https://github.com/mdLafrance/grepenv/actions/workflows/pipeline.yaml)
  
</div>

## About
A simple tool to search through your environment.  
Provides additional options for highlighting, searching specifically keys or values, and extracting values from best match keys.

> You can achieve similar results with a one liner bash alias, but after having rewritten that alias on every machine I've used, I decided to turn it into a package.


## Installation
`grepenv` can be installed using pip, but [pipx]([pipx](https://github.com/pypa/pipx)) is recommended:
```bash
pipx install grepenv
```
This installs the `grepenv` shell script:
```bash
grepenv --help
```
## Usage
`grepenv` takes a regex pattern, and matches it against currently available environment variables.  
Calling `grepenv --example` will show some example usage.

```bash
$ grepenv xdg # Will find any key or value that contains the letters xdg (lower or upper case).
```

``` bash
$ grepenv "_api_(key|token)_" -k # finds any environment that looks like an api key. Searches only keys.
GITHUB_API_TOKEN=abc_NlNhalNDL78NAhdKhNAk78bdf7f
OPENAI_API_KEY=123_abcdefghijklmno
```

```bash
$ grepenv -fk git # find-key 'git'- finds all keys matching the pattern 'git' and gets their values.
123_abcdefghijklmnop
```
