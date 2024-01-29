# Task 5 Python Package by Anton Galkin



## Description

The package contains a program that counts the number of authentic characters in a string.<br/>
To download data, you can specify the following parameters
when starting the program in the terminal: <br/>
  --string "your string" <br/>
  --file path_your_file <br/>

Example of import in python console:<br/>
  `>>>` from task_5_python_package_by_AG import count_authentic_signs

Example of import in CLI:<br/>
  python -c 'from task_5_python_package_by_AG import cli(); cli()' --string "aabcdeefff"<br/>

  python -c 'from task_5_python_package_by_AG import cli(); cli()' --file home/anton/Documents/test-text

## Project structure

task_5_python_package <br/>
│ <br/>
├── application <br/>
│ ├── `__init.py__` <br/>
│ └── app.py <br/>
│<br/>
└── `__main__.py` <br/>

## Installation

Input in your terminal next:
```
python3 pip install task_5_python_package_by_AG
```

## Usage

For use application you can to use Command Line Interface.

Use to read lines in terminal:
```
python -m task_5_python_package_by_AG --string "your string"
```

Use to read lines in a file:
```
python -m task_5_python_package_by_AG --file path_your_file
```

***

## Authors and acknowledgment
Anton Galkin

## License
MIT

## Project status
Study
