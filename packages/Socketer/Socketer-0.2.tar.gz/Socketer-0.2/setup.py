from setuptools import setup, find_packages

setup(
  name="Socketer",
  version='0.2',
  packages=find_packages(),
  requires=[

  ],
  entry_point={
    "console_scripts": [
      "Socketer-hello = Socketer:hello"
    ],
  },
)