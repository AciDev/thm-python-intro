from base64 import b16decode, b32decode, b64decode, b16encode, b32encode, b64encode
import codecs


def isBase16(sb):
    try:
        if isinstance(sb, str):
            sb_bytes = bytes(sb, 'ascii')
        elif isinstance(sb, bytes):
            sb_bytes = sb
        else:
            raise ValueError("Argument must be string or bytes")
        return b16encode(b16decode(sb_bytes)) == sb_bytes
    except Exception:
        return False


def isBase32(sb):
    try:
        if isinstance(sb, str):
            sb_bytes = bytes(sb, 'ascii')
        elif isinstance(sb, bytes):
            sb_bytes = sb
        else:
            raise ValueError("Argument must be string or bytes")
        return b32encode(b32decode(sb_bytes)) == sb_bytes
    except Exception:
        return False


def isBase64(sb):
    try:
        if isinstance(sb, str):
            sb_bytes = bytes(sb, 'ascii')
        elif isinstance(sb, bytes):
            sb_bytes = sb
        else:
            raise ValueError("Argument must be string or bytes")
        return b64encode(b64decode(sb_bytes)) == sb_bytes
    except Exception:
        return False


def detectBaseEncoding(s):
    if(isBase16(s)):
        return b16decode(s)
    elif(isBase32(s)):
        return b32decode(s)
    elif(isBase64(s)):
        return b64decode(s)
    else:
        return False


def main():
    file = open('./encodedflag.txt', 'r').read()
    decoding = detectBaseEncoding(file)
    while decoding != False:
        decoding = detectBaseEncoding(decoding)
        if type(decoding) == bytes:
            flag = decoding
        else:
            flag = flag

    print(flag.decode())


if __name__ == "__main__":
    main()
