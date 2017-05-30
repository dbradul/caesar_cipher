# Caesar cipher

Demonstrates Python basics with simple example of encrypting/decrypting using Caesar cipher (https://en.wikipedia.org/wiki/Caesar_cipher). 

### To collect letters frequency:
```
python3 demo.py
```

### To encrypt using "Caesar cipher":
```
python3 encrypt.py <input> <output> <offset>
```
- `input`: input file to be encrypted
- `output`: output encrypted file
- `offset`: offset used for encryption

Example:
```
python3 encrypt.py hhgttg.txt hhgttg_enc.txt 99
```


### To break "Caeser cipher":
```
python3 encrypt.py <ref> <input> <output>
```
- `ref`: reference file to calculate English letters frequency
- `input`: input encrypted file
- `output`: output decrypted file

Example:
```
python3 decrypt.py alice.txt hhgttg_enc.txt hhgttg_decr.txt
```
