from setuptools import setup, find_packages

setup(name="plasmarl",
      version="0.0.1",
      description="plasmarl",
      url="https://github.com/danielsuo/plasmarl",
      author="Daniel Suo",
      license="MIT",
      packages=find_packages(),
      install_requires=[
          "numpy",
          "scipy",
          "jupyter",
          "ipython",
          "flake8",
          "matplotlib",
          "pandas",
          "scikit-learn",
          "click",
          "requests",
          "tqdm",
          "theano",
          "keras",
          "clickutil"
      ])
