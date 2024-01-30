# Prepaid Sim Py Client
Python package to retrieve prepaid sim remaining data usage.


## Example 

```shell
from prepaid_sim_py_client_xethhung12.hk.csl import remainingAmountOfData
if __name__ == '__main__':
    mobileNo = "{mobileNo}"
    password = "{password}"
    print(remainingAmountOfData(mobileNo, password))
```

## Build
```shell
rm -fr dist
python -m build
```

## Upload
```shell
rm -fr dist
python -m build
twine upload dist/*

```