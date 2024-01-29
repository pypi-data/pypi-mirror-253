# Pipeline automation framework for Python

## Install

### From PyPi (for users)

```
pip install pysquared
```

### From GitLab (for developers of the library)

Clone repo with

```
git clone --recursive https://gitlab.com/knvvv/pysquared.git
```

```
conda env create -n pysquared-test -f environment.yaml
conda activate pysquared-test
```

Then, run your scripts in this directory or include these lines at the beginning of you script:

```
import sys
sys.path.append('/path/to/repo/pysquared')
```


## Release PyPi package

```
python setup.py sdist
twine upload dist/*
```
