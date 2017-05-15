# Python demo

Demonstrates Python basics with 2 examples. 

## To collect letters frequency:
```
python3 demo.py
```

## To encrypt using "Caesar cipher":
```
python3 encrypt.py <input> <output> <offset>
```
- `input`: input filename for a file to be encrypted
- `output`: output file name fo encrypted file
- `offset`: offset to use for encryption

Example:
```
python3 encrypt.py hhgttg.txt hhgttg_enc.txt
```


## To break "Caeser cipher":
```
python3 encrypt.py <ref> <input> <output>
```
- `ref`: file to be used as reference to calculate English letters frequency
- `input`: input filename for a file to be decrypted
- `output`: output filename for a decrypted file

Example:
```
python3 decrypt.py alice.txt hhgttg_enc.txt hhgttg_decr.txt
```
