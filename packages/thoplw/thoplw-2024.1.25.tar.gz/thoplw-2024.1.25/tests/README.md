Test thoplw package
================================================================================

This directory contains code to test the `thoplw` module.


Build environment
--------------------------------------------------------------------------------

```console
# Create new virtual environment.
python3 -m venv venv

# Activate the virtual environment.
source venv/bin/activate

# Confirm your virtual environment works correctly.
which python3

# Upgrade pip.
python3 -m pip install --upgrade pip

# Install packages.
python3 -m pip install -r requirements.txt
```


Run the test code
--------------------------------------------------------------------------------

Before running the test code, please activate the virtual environment.

```console
# Activate the virtual environment.
source venv/bin/activate

# Confirm your virtual environment works correctly.
which python3
```

### Benchmarks on CNN models

```python
python3 test_benchmarks.py
```

### Comparison with thop

```python
python3 test_comparison_with_thop.py
```

