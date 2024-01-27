# env-colab-pass
Python module that check for key value in env and colab userdata. if not found then asks for it using getpass

#Usage 

## Install package
```
pip install env-colab-pass
```

## Import module 
```
from env_colab_pass import passutil 
```

## To get the value of a env variable / colab user data / ask user 

```
passutil.get_secret_value(key_name)
```
