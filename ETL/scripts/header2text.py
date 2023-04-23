"""
convert header to text for secret keeping
"""
def header2text():
    import pyperclip

    headersList: dict[str, str] = {}
    cb = pyperclip.paste()

    # headersList updated
    exec(cb)

    # convert to pickle byte
    import pickle
    from io import BytesIO

    with BytesIO() as f:
        pickle.dump(headersList, f)
        pickleByte = f.getvalue()

    # convert to base64
    import base64

    base64Byte = base64.b64encode(pickleByte)

    # copy to clipboard
    pyperclip.copy(base64Byte.decode("utf-8"))

    print("Copied to clipboard")

def text2header(text):
    import base64
    import pickle
    from io import BytesIO

    base64Byte = text.encode("utf-8")
    pickleByte = base64.b64decode(base64Byte)

    with BytesIO(pickleByte) as f:
        headersList = pickle.load(f)

    return headersList

if __name__ == "__main__":
    header2text()