from setuptools import setup, find_packages

setup(name="plasma-rl",
      version="0.0.1",
      description="plasma-rl",
      url="https://github.com/danielsuo/plasma-rl",
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
          "keras",
          "clickutil"
      ])
