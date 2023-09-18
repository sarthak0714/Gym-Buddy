from kellanb_cryptography import easy


def encrypt(passw):
    print(easy.encrypt(passw, "wegojim"))
    return easy.encrypt(passw, "wegojim")


def decrypt(passw):
    print(easy.decrypt(passw, "wegojim"))
    return easy.decrypt(passw, "wegojim")


if __name__ == '__main__':
    print("hello")
