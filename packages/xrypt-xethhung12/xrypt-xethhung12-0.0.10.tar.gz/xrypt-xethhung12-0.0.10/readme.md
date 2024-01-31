# Installation
```shell
pip install -U xrypt-xethhung12
```

# Usage
```shell
from xrypt_xethhung12.rsa_encryption import gen_key_pair, read_public_key_from_pem_str, read_private_key_from_pem_str
from xrypt_xethhung12.rsa_format import pub_key_to_pem, pri_key_to_pem
from xrypt_xethhung12.xrypt.xrypt import DeEnCryptor, Signer, Verifier

if __name__ == '__main__':
    # Generate key pair
    s_pub, s_pri = gen_key_pair()
    r_pub, r_pri = gen_key_pair()

    # encrypt and decrypt
    data_encrypted = DeEnCryptor(s_pub, s_pri).encryptToContainer(r_pub, "helloworld")
    data = DeEnCryptor(r_pub, r_pri).decryptContainer(s_pub, data_encrypted)
    print(data)

    # sign and verify
    signed_data = Signer(s_pri).sign("helloworld")
    print(Verifier(s_pub).verify(signed_data))

    # To pem format string
    print(pub_key_to_pem(s_pub))
    print(pri_key_to_pem(s_pri))

    reloaded_s_pub_key = read_public_key_from_pem_str(pub_key_to_pem(s_pub))
    reloaded_s_pri_key = read_private_key_from_pem_str(pri_key_to_pem(s_pri))
    reloaded_r_pub_key = read_public_key_from_pem_str(pub_key_to_pem(r_pub))
    reloaded_r_pri_key = read_private_key_from_pem_str(pri_key_to_pem(r_pri))

    # encrypt and decrypt - again
    data_encrypted = DeEnCryptor(reloaded_s_pub_key, reloaded_s_pri_key).encryptToContainer(reloaded_r_pub_key, "helloworld")
    data = DeEnCryptor(reloaded_r_pub_key, reloaded_r_pri_key).decryptContainer(reloaded_s_pub_key, data_encrypted)
    print(data)

    # sign and verify - again
    signed_data = Signer(reloaded_s_pri_key).sign("helloworld")
    print(Verifier(reloaded_s_pub_key).verify(signed_data))
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
