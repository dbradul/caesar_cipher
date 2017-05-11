import sys
import string

#------------------------------------------------------------
def encrypt_text(text, key):
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
    fd_in = open(sys.argv[1])

    key = 99
    encrypted = encrypt_text(fd_in.read().lower(), key)

    fd_out = open(sys.argv[2], "w")
    fd_out.write(encrypted)
    fd_out.close()