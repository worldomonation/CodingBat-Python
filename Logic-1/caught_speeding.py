# Tested 2016-06-19 00:50

def caught_speeding(speed, is_birthday):
    # the birthday modifier increases speed limit by 5.
    # in essence, your speed decreases by 5.
    if is_birthday:
            speed-=5
    if speed <= 60:
            return 0
    elif speed <= 80:
            return 1
    else:
            return 2
