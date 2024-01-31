from setuptools import setup, find_packages

setup(
  name="Socketer",
  version='0.3',
  packages=find_packages(),
  requires=[

  ],
  command_options={
    "console_scripts": [
      "Socketer-hello = Socketer:hello"
    ],
  },
)