# Libraries
A library is just another file (or many files)
of python code that is magically brought into
your own file using just one line

```python
import random # random is the name of the library
# then we can use the "randint" function in the
# "random" library
x = random.randint(0, 5)
```

# 3rd party libraries
To use a 3rd party library we need to install it
using pythons built in "package manager"

Python uses "Pip"
```sh
# how to install a library
python -m pip install pandas # installs pandas
```

# VENV
Sometimes we need to keep the libraries
in the same project to keep from breaking
system packages
```sh
# creates a virtual environment folder named: venv
python -m venv venv
`
# activate the environment`
# Windows:
.\venv\Scripts\Activate.ps1
# MacOS:
source ./venv/bin/activate
```