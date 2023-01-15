# Build-Python-PyPi_Project

This is a tutorial on how to build a Python .whl package.

# Directories
<pre>
├─pyproject.toml  
│
├─LICENSE
│
├─README.Md
│
├─src
|   ├─Package_Dir(diseasesClassification)
|                ├─__init__.py
│                |
|                ├─pythonfile.py
|
</pre>


## Creating pyproject.toml
```
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```
OR
```
[build-system]
requires = ["setuptools>=43.0.0", "wheel"]
build-backend = "setuptools.build_meta"
```

## Configuring metadata

```
[project]
name = "package_name"
version = "0.0.1"
authors = [
  { name="Example Author", email="author@example.com" },
]
description = "A small example package"
readme = "README.md"
requires-python = ">=3.7"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

[project.urls]
"Homepage" = "https://github.com/HSAkash/Build-Python-PyPi_Project"
"Bug Tracker" = "https://github.com/HSAkash/Build-Python-PyPi_Project/issues"
```


### pyproject.toml file
```
[project]
name = "package_name"
version = "0.0.1"
authors = [
  { name="Example Author", email="author@example.com" },
]
description = "A small example package"
readme = "README.md"
requires-python = ">=3.7"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

[project.urls]
"Homepage" = "https://github.com/HSAkash/Build-Python-PyPi_Project"
"Bug Tracker" = "https://github.com/HSAkash/Build-Python-PyPi_Project/issues"


[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```


## Creating README.md

```
# Package name
[Profile](https://github.com/HSAkash)
```

## Creating a LICENSE

```
MIT License

Copyright (c) 2023 HSAkash

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```


## Generating distribution archives
Install build package
```
python3 -m pip install --upgrade build
```

Now run this command from the same directory where pyproject.toml is located:
```
python3 -m build
```

This command should output a lot of text and once completed should generate two files in the dist directory:

<pre>
├─pyproject.toml  
│
├─LICENSE
│
├─README.Md
│
├─src
|   ├─Package_Dir(diseasesClassification)
|                ├─__init__.py
│                |
|                ├─pythonfile.py
|
│
├─dist
│   ├─ packageName-version.whl
|   |
|   ├─packageName-version.tar.gz
|
</pre>

## Uploading 
First create account on [link]( https://test.pypi.org)
Install twine
```
python3 -m pip install --upgrade twine
```
Uploading
```
python3 -m twine upload --repository testpypi dist/*
```

## Installing packages from sources
```python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps package_name```
```python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps package_name==verion```
```python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps package_name==0.0.1```


## Run or call the package
```
python3
```
and import the package:
```
>>> from packagename import function_or_classname
>>> call_function(parameters)
```

## Get Help or more information
[click](https://packaging.python.org/en/latest/tutorials/packaging-projects/)