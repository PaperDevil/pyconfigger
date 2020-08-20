# Python Configger
A package for flexible configuration of all your projects.
Supports JSON and YAML config files.

## Installation
```pip install py-configger```

## Usage
The main tools provided by the package are the BasicConfig and SingleConfig classes.
#### BasicConfig
Standard config implementation. Its peculiarity is the ability to be defined only in one place, and then be passed to factories as an argument or imported by other modules.
```.python
from configger import BasicConfig

basic_config = BasicConfig("config.yml")

print(basic_config['version'])
print(basic_config('version').value)
```

#### SingleConfig
Config type implementing the Singleton pattern. You can get the same version of your config anywhere in your project.

**main.py**
```.python
from configger import SingleConfig
from second import do_stuff


single_config = SingleConfig("config.json")
single_config['color'] = 'orange'

do_stuff()
```

**second.py**
```.python
from configger.config import SingleConfig

def do_stuff():
    config = SingleConfig(show_config=True)
```
## Todo List
    - Expand functionality to access other types of config files
    - Add the ability to create nested fields
    - Retrieving a config file by URL
