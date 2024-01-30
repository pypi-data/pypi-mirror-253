# Installation
```shell
pip install -U xrypt-xethhung12
```

# Usage
```shell
import json
from xrypt_xethhung12.xrypt.xrypt import read_public_key_from_pem, read_private_key_from_pem, DeEnCryptor


def load_file(file_path: str) -> dict:
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    base_path = "./"
    s_pub = read_public_key_from_pem(base_path + "s_pub.key")
    s_pri = read_private_key_from_pem(base_path + "s_pri.key")
    r_pub = read_public_key_from_pem(base_path + "r_pub.key")
    r_pri = read_private_key_from_pem(base_path + "r_pri.key")
    d = load_file(base_path + "encrypted-data")

    deen = DeEnCryptor(s_pub, s_pri)
    container = deen.encryptToContainer(r_pub, "helloworld")
    containerStr = deen.encryptToJsonContainer(r_pub, "helloworld")
    print(containerStr)

    deen = DeEnCryptor(r_pub, r_pri)
    print(deen.decryptContainer(s_pub, container))
```

# Scripts

## Generate rsa key pair
```shell
pri={pri}
pub={pub}
openssl genrsa -out $pri 4096
openssl rsa -in $pri -outform PEM -pubout -out $pub
```

## Build 
```shell
rm -fr dist
python3 -m build
```


## Build and Deploy
```shell
rm -fr dist
python3 -m build
twine upload dist/* -u __token__ -p $pwd
```

## Update version dev
```shell
python3 -m xh_py_project_versioning --patch
```

## Update version
```shell
python3 -m xh_py_project_versioning --patch -d
```
