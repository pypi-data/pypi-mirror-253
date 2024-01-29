# Pipeline automation framework for Python

## Install

Clone repo with

```
git clone --recursive https://gitlab.com/knvvv/autopy.git
```

setup.py is coming soon... Until then, install prerequisites with

```
conda env create -n autopy-test -f environment.yaml
conda activate autopy-test
```

Then, run your scripts in this directory or include these lines at the beginning of you script:

```
import sys
sys.path.append('/path/to/repo/autopy')
```
