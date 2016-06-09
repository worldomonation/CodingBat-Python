def xyz_there(str):
    if len(str) < 3:
        return False
    # replace the offending string with a character (or string) that is unlikely to occur.
    # acceptable risk in the context of codingbat assignments, but risky in production.
    str = str.replace('.xyz', '!')
    if str.count('xyz') > 0:
        return True
    return False
