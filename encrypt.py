import sys
import string

#------------------------------------------------------------
def encrypt_text(text, key):
    '''
    Encrypts text using Ceaser cipher (http://bit.ly/1FL5OA4)
    :param text: Text to encrypt
    :param key:  Offset to shift a letter
    :return: Enripted text
    '''
    encrypted = ""

    for c in text:
        encr_ch = c

        if c in string.ascii_lowercase:
            # encr_code = ord(c)+offset
            encr_code = ord('a') + (ord(c) + key) % len(string.ascii_lowercase)
            encr_ch = chr(encr_code)

        encrypted += encr_ch

    return encrypted

#------------------------------------------------------------
if __name__ == "__main__":
    # command line arguments
    filename_original = sys.argv[1]
    filename_encryptd = sys.argv[2]
    key               = int(sys.argv[3])

    # encrypt
    with open(filename_original) as f:
        encrypted = encrypt_text(f.read().lower(), key)

    # save encrypted text
    with open(filename_encryptd, "w") as f:
        f.write(encrypted)
