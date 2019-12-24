#!/usr/bin/env bash

pip install -e .

git clone https://github.com/PPPLDeepLearning/plasma-python
pushd plasma-python
python setup.py install
popd
