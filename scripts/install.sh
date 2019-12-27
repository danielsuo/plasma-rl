#!/usr/bin/env bash

pip install -e .

mkdir -p deps

pushd deps

if [ ! -d plasma-python ]; then
  git clone https://github.com/PPPLDeepLearning/plasma-python
  pushd plasma-python
  pip install -e .
  popd
fi

if [ ! -d TigerForecast ]; then
  git clone https://github.com/MinRegret/TigerForecast
  pushd TigerForecast
  pip install -e .
  popd
fi

popd
