# Gendiff
---
### Hexlet tests and linter status:
[![Actions Status](https://github.com/marinavasyukova/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/marinavasyukova/python-project-50/actions) [![Python CI](https://github.com/marinavasyukova/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/marinavasyukova/python-project-50/actions/workflows/pyci.yml) [![Maintainability](https://api.codeclimate.com/v1/badges/3faf578b85ebd40d3eba/maintainability)](https://codeclimate.com/github/marinavasyukova/python-project-50/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/3faf578b85ebd40d3eba/test_coverage)](https://codeclimate.com/github/marinavasyukova/python-project-50/test_coverage)

---

## Description
**Gendiff** is a program for comparing two data structures

Features of utility:
- Supported formats: JSON, YAML
- Report generation as plain text, structured text (stylish format) and JSON format
- Usage as CLi-utility or external library

    
    It's the second training project on Hexlet 'Python developer' course.
---

## Installation

1. ### Using pip
    ```bash
    python3 -m pip install --user git+https://github.com/marinavasyukova/python-project-50.git
    ```
or

2. ### Download from git repository
    1. Clone the repository
    ```bash
    git clone https://github.com/marinavasyukova/python-project-50.git
    ```
    2. Go to the project directory
    ```bash
    cd python-project-50
    ```

    3. Install the program

    ```bash
    make setup
    ```
---

## Usage

### **Cli-utility**
```bash
% gendiff -h          
usage: gendiff [-h] [-f {plain,stylish,json}] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file            path to the first file
  second_file           path to the second file

options:
  -h, --help            show this help message and exit
  -f {plain,stylish,json}, --format {plain,stylish,json}
                        set format of output (default: "stylish")
```

### **Library**
```python
from gendiff import generate_diff

diff = generate_diff(file_path1, file_path2)
print(diff)
```

---
## Demo

<details>
<summary>Example of 2 plain .json files comparison (stylish format)</summary>

```bash
% gendiff file1.json file2.json
```

[![asciicast](https://asciinema.org/a/Cy9uLmqjrE5rM03Qc2Ygk41Wi.svg)](https://asciinema.org/a/Cy9uLmqjrE5rM03Qc2Ygk41Wi)
</details>

<details>
<summary>Example of 2 plain .yaml files comparison (stylish format)</summary>

```bash
% gendiff file1.yaml file2.yaml
```

[![asciicast](https://asciinema.org/a/AqCDguTgp1OxjR1L77ysIsWak.svg)](https://asciinema.org/a/AqCDguTgp1OxjR1L77ysIsWak)
</details>

<details>
<summary>Example of 2 nested .json and .yaml files comparison (stylish format)</summary>

```bash
% gendiff file1.json file2.json
% gendiff file1.yaml file2.yaml
```

[![asciicast](https://asciinema.org/a/YrWLFAivqtkD5IuWA0VMnG5Km.svg)](https://asciinema.org/a/YrWLFAivqtkD5IuWA0VMnG5Km)
</details>

<details>
<summary>Example of 2 nested .json and .yaml files comparison in 2 different formats (stylish and plain)</summary>

```bash
% gendiff file1.json file2.json
% gendiff file1.json file2.json -f plain
% gendiff file1.yaml file2.yaml
% gendiff file1.yaml file2.yaml -f plain
```

[![asciicast](https://asciinema.org/a/UtOyI1DLF6mM6M9z4ealUw10e.svg)](https://asciinema.org/a/UtOyI1DLF6mM6M9z4ealUw10e)
</details>

<details>
<summary>Example of 2 nested .json and .yaml files comparison in json format</summary>

```bash
% gendiff file1.json file2.json -f json
% gendiff file1.yaml file2.yaml -f json
```

[![asciicast](https://asciinema.org/a/KVkG7T5YNyolZkOkoPGCcASj3.svg)](https://asciinema.org/a/KVkG7T5YNyolZkOkoPGCcASj3)
</details>