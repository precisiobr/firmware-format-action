# Nordian clang-format action

Runs clang-format and emits an error when finding ill formatted files.\
It assumes the calling repository has a `.clang-format` style file.

## Sample usage

```yml
name: "Verify formatting"

on:
  pull_request:
    branches:
      - main

jobs:
  format:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: precisiobr/firmware-format-action@v1
```

### Details
Python version = 3.10\
clang-format version = 18.1.6
